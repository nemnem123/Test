import boto3
import os

class EchoRepository:
    def __init__(self):
        dynamodb = boto3.resource('dynamodb')
        table_name = os.environ.get('TABLE_NAME', 'EchoTable')
        self.table = dynamodb.Table(table_name)

    def save(self, item):
        self.table.put_item(Item=item)

    def get_all(self):
        response = self.table.scan()
        return response.get('Items', [])

    def delete(self, item_id):
        self.table.delete_item(Key={"id": item_id})