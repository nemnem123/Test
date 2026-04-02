import pytest
import os
from unittest.mock import MagicMock
from repositories.echo_repo import EchoRepository

def test_save_item_to_dynamodb(mocker):
    # 1. Chuẩn bị: Giả lập (Mock) thư viện boto3 để không gọi lên AWS thật
    mock_boto3 = mocker.patch('repositories.echo_repo.boto3.resource')
    mock_table = MagicMock()
    mock_boto3.return_value.Table.return_value = mock_table
    
    # Thiết lập biến môi trường giả cho tên bảng
    os.environ['TABLE_NAME'] = 'TestTable'
    
    repo = EchoRepository()
    test_item = {"id": "123", "data": {"message": "hello"}}
    
    # 2. Hành động: Gọi hàm save của Repo
    repo.save(test_item)
    
    # 3. Kiểm tra: Đảm bảo hàm put_item của DynamoDB được gọi đúng dữ liệu
    mock_table.put_item.assert_called_once_with(Item=test_item)

def test_get_all_items_from_dynamodb(mocker):
    # Giả lập hàm scan của DynamoDB
    mock_boto3 = mocker.patch('repositories.echo_repo.boto3.resource')
    mock_table = MagicMock()
    mock_boto3.return_value.Table.return_value = mock_table
    
    # Giả lập dữ liệu trả về từ DB
    mock_table.scan.return_value = {"Items": [{"id": "1"}, {"id": "2"}]}
    
    repo = EchoRepository()
    results = repo.get_all()
    
    # Kiểm tra xem có lấy đủ 2 item không
    assert len(results) == 2
    mock_table.scan.assert_called_once()

def test_delete_item_from_dynamodb(mocker):
    # Mock DynamoDB
    mock_boto3 = mocker.patch('repositories.echo_repo.boto3.resource')
    mock_table = MagicMock()
    mock_boto3.return_value.Table.return_value = mock_table
    
    repo = EchoRepository()
    test_id = "123-abc"
    
    # Hành động: Gọi hàm delete
    repo.delete(test_id)
    
    # Kiểm tra: Đảm bảo Repo đã gọi lệnh delete_item với đúng ID
    mock_table.delete_item.assert_called_once_with(Key={"id": test_id})