# DTDM-Nhom23
Tìm hiểu về Amazon Rekognition và viết ứng dụng minh họa (sử dụng ngôn ngữ Python)
## Hướng dẫn cài đặt

###B1: Cấp quyền cho EC2 có thể kết nối vào S3 Bucket bằng cách thay đổi IAM role của nó. Ở đây chúng tôi thêm AmazonS3FullAccess Policy vào EMR_EC2_DefaultRole và cấp role đó cho EC2

###B2: Tắt Block all public access của S3 Bucket được sử dụng bằng cách vào mục Permissions của S3 Bucket đó

###B3: Kết nối SSH vào EC2, tạo một thư mục có tên bất kỳ để chứa venv và thư mục flask app
###B4: Tiến hành cài đặt Python Virtualenv bằng lệnh
  - sudo apt-get update
  - sudo apt-get install python3.7
  - sudo sudo apt-get install python3.7-venv
Nếu gặp lỗi, có thể tham khảo tại đây: https://askubuntu.com/questions/1109982/e-could-not-get-lock-var-lib-dpkg-lock-frontend-open-11-resource-temporari

###B5:Tại thư mục trên, tiến hành thực thi lệnh git clone https://github.com/ztank01/DTDM-Nhom23.git, sau khi hoàn thành ta cài đặt venv bằng lệnh python3.7 -m venv venv. Sau đó ta kích hoạt môi trường bằng lệnh source venv/bin/activate, tiến hành cài đặt các thư viện cần thiết bằng lệnh pip install -r DTDM-Nhom23/requirements.txt. Cuối cùng, ta thử chạy main.py trong thư mục DTDM-Nhom23 được clone về trên local bằng lệnh python main.py, nếu thành công ta chuyển sang bước tiếp theo

###B6: Cài đặt Gunicorn sử dụng -  $ pip install gunicorn. Sau đó, chạy Gunicorn — $ gunicorn -b 0.0.0.0:8000 main:app


Hướng dẫn cài đặt được tham khảo từ: https://medium.com/techfront/step-by-step-visual-guide-on-deploying-a-flask-application-on-aws-ec2-8e3e8b82c4f7
