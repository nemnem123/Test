import sys
import os

# 1. Bẻ đường dẫn cho Pytest nhận diện thư mục lambda
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../lambda')))

# 2. Cấp thông tin AWS giả mạo cho toàn bộ môi trường Test
# Việc này đảm bảo boto3 không báo lỗi NoRegionError và KHÔNG BAO GIỜ gọi nhầm vào AWS thật làm tốn tiền
os.environ['AWS_DEFAULT_REGION'] = 'ap-southeast-1'
os.environ['AWS_ACCESS_KEY_ID'] = 'testing'
os.environ['AWS_SECRET_ACCESS_KEY'] = 'testing'
os.environ['AWS_SECURITY_TOKEN'] = 'testing'
os.environ['AWS_SESSION_TOKEN'] = 'testing'