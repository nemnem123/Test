import pytest
from services.echo_service import EchoService

def test_create_echo(mocker):
    # Dùng mocker chặn hàm 'save' của EchoRepository. 
    # Logic: "Giả vờ như đã lưu DB thành công, không cần gọi DB thật"
    mock_save = mocker.patch('services.echo_service.EchoRepository.save')
    
    service = EchoService()
    input_data = {"hello": "world"}
    
    # Hành động
    item_id, result_item = service.create_echo(input_data)
    
    # Kiểm tra
    assert item_id is not None
    assert type(item_id) is str
    assert result_item["data"] == input_data
    
    # Đảm bảo Service đã ra lệnh gọi hàm save() của Repo đúng 1 lần với data chuẩn
    mock_save.assert_called_once_with(result_item)