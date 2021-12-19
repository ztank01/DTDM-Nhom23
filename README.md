# DTDM-Nhom23
Tìm hiểu về Amazon Rekognition và viết ứng dụng minh họa (sử dụng ngôn ngữ Python)
## Hướng dẫn cài đặt

### B1: Cấp quyền cho EC2 có thể kết nối vào S3 Bucket bằng cách thay đổi IAM role của nó. Ở đây chúng tôi thêm AmazonS3FullAccess Policy vào EMR_EC2_DefaultRole và cấp role đó cho EC2

### B2: Tắt Block all public access của S3 Bucket được sử dụng bằng cách vào mục Permissions của S3 Bucket đó

### B3: Kết nối SSH vào EC2, tạo một thư mục có tên bất kỳ để chứa venv và thư mục flask app

### B4: Tiến hành cài đặt Python Virtualenv bằng lệnh<br>
  - sudo apt-get update<br>
  - sudo apt-get install python3.7<br>
  - sudo sudo apt-get install python3.7-venv<br>
Nếu gặp lỗi, có thể tham khảo tại đây: https://askubuntu.com/questions/1109982/e-could-not-get-lock-var-lib-dpkg-lock-frontend-open-11-resource-temporari

### B5:Tại thư mục trên, tiến hành thực thi lệnh git clone https://github.com/ztank01/DTDM-Nhom23.git, sau khi hoàn thành ta cài đặt venv bằng lệnh python3.7 -m venv venv. Sau đó ta kích hoạt môi trường bằng lệnh source venv/bin/activate, tiến hành cài đặt các thư viện cần thiết bằng lệnh pip install -r DTDM-Nhom23/requirements.txt. Cuối cùng, ta thử chạy main.py trong thư mục DTDM-Nhom23 được clone về trên local bằng lệnh python main.py, nếu thành công ta chuyển sang bước tiếp theo

### B6: Cài đặt Gunicorn sử dụng -  $ pip install gunicorn. Sau đó, chạy Gunicorn — $ gunicorn -b 0.0.0.0:8000 main:app. Nếu thành công ta chuyển sang bước tiếp theo

### B7:Chúng ta sẽ tạo <projectname>.service file trong thư mục /etc/systemd/system bằng lệnh - $ sudo vi /etc/systemd/system/<projectname>.service. với projectname nên trùng với tên thư mục đã được tạo ở B3. <projectname>.service có nội dung như sau:
  
  <p>[Unit]<br>
  Description=Gunicorn instance for a simple hello world app<br>
  After=network.target
  </p>
  
  </p>[Service]<br>
  User=ubuntu<br>
  Group=ubuntu <thay đổi tùy theo user chúng ta đang sử dụng thuộc group nào><br>
  WorkingDirectory=/home/ubuntu/<thư mục được tạo tại bước 3>/DTDM-Nhom23<br>
  ExecStart=/home/ubuntu/<thư mục được tạo tại bước 3>/venv/bin/gunicorn -b localhost:8000 main:app<br>
  Restart=always<br>
  </p>
  
  <p>[Install]<br>
  WantedBy=multi-user.target<br>
  </p>

Cuối cùng kích hoạt service mới được tạo<br>
  $ sudo systemctl daemon-reload<br>
  $ sudo systemctl start <projectname><br>
  $ sudo systemctl enable <projectname><br>
 Kiểm tra ứng dụng có chạy không bằng lệnh $ curl localhost:8000<br>
  
 ### B8: Cài đặt Nginx bằng $ sudo apt-get install nginx, Sau đó chạy các lệnh<br>
  $ sudo systemctl start nginx<br>
  $ sudo systemctl enable nginx<br>
 Nếu thành công, khi ta truy cập vào Public IPv4 Address của EC2 sẽ hiện lên trang mặc định của nginx<br>
  
 ### B9: Cấu hình lại Nginx
 Chỉnh sửa lại file mặc định trong thư mục sites-available bằng lệnh <br>
  $ sudo vi /etc/nginx/sites-available/default <br>
Thêm đoạn code sau vào trên cùng của file<br>
  upstream flaskhelloworld {<br>
    server 127.0.0.1:8000;<br>
}<br>
Thêm proxy_pass đến flaskhelloworld tại location /<br>
  #Some code above<br>
location / {<br>
    proxy_pass http://flaskhelloworld;<br>
}<br>
#some code below<br>
  
Khởi động lại  Nginx — $ sudo systemctl restart nginx<br>
  
Bây giờ nếu ta truy cập vào Public IPv4 Address của EC2 sẽ hiện lên website của chúng ta

Hướng dẫn cài đặt được tham khảo từ: https://medium.com/techfront/step-by-step-visual-guide-on-deploying-a-flask-application-on-aws-ec2-8e3e8b82c4f7
