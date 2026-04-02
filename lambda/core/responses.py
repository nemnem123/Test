import json

def build_response(status_code, body):
    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(body)
    }
// Đây là một hàm tiện ích để xây dựng response chuẩn cho API Gateway
// Nó giúp đảm bảo mọi response đều có cấu trúc giống nhau và dễ dàng chỉnh sửa
