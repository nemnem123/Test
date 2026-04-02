import uuid
from repositories.echo_repo import EchoRepository

class EchoService:
    def __init__(self):
        self.repo = EchoRepository()

    def create_echo(self, data):
        item_id = str(uuid.uuid4())
        item = {
            "id": item_id,
            "data": data
        }
        self.repo.save(item)
        return item_id, item

    def get_all_echos(self):
        return self.repo.get_all()

    def delete_echo(self, item_id):
        self.repo.delete(item_id)