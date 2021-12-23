# from PIL import Image
import boto3
from flask import Flask, request, render_template
import rekognition

aws_access_key_id = "ASIAQYD45YXPBBP22W3Z"
aws_secret_access_key = "McRGqLEuNqnp4IEcxCelxWdwoHeyvwzSOyp//E4M"
aws_session_token = "FwoGZXIvYXdzEFoaDIqaEPHjsHsFDV1s1yLKAUF0Uhg+bt8t5cWoqelNTbQQ69WoeI1GvE9yuGlCEyGh/WDz6janD2bjfPOaXoYhUsEWOWM5czhRi9Gwu205zhtEHPw81QgXopBtQ5Ppk6zEy+9C1g/PuGhMW1rjJU8B+slAVQoMn1s94DfVZLNtLPESzBuBTlo424VLgNIF0nW4ZtJrBqJNtlwfGeQxWuKWWD1RUrMyi927rk09c42YRtbiVVTENyogHmzsvK6j7wxQjqCQRA8IovhK1a/7+HNJcGWgHMUwqRZOCE0o8tuQjgYyLYJDfIGFYDJVjCP/IOBfqb1BvbVQo0BJTjYbicQ9H7trjArYllLmBRbIb3j6+g=="


app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads/'
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


@app.route('/')
def upload_form():
    return render_template('home.html')


@app.route('/khuonmat')
def ptkhuonmat():
    return render_template('upload_khuonmat.html')


@app.route('/object')
def ptobject():
    return render_template('upload_image.html')


@app.route('/baoho')
def ptbaoho():
    return render_template('upload_baoho.html')


@app.route('/uploadobject', methods=['post'])
def upload_object():
    global aws_access_key_id
    global aws_secret_access_key
    global aws_session_token
    avatar = request.files.get("file")
    s3 = boto3.resource(
        service_name='s3',
        region_name='us-east-1',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        aws_session_token=aws_session_token)  # for bucket in s3.buckets.all():
    # return bucket.name
    if avatar:
        avatar.save("%s/static/images/%s" % (app.root_path, avatar.filename))
    # return "SUCCESSFUL"
    # return "FAIL"
    s3.Bucket('rekognition3').upload_file("static/images/" + avatar.filename, avatar.filename)
    rekognitionImage = rekognition.detect_labels(avatar.filename, 'rekognition3')
    return render_template("rekognition_object.html", avatar=avatar.filename, rekog=rekognitionImage)


@app.route('/uploadkhuonmat', methods=['post'])
def upload_km():
    global aws_access_key_id
    global aws_secret_access_key
    global aws_session_token
    avatar = request.files.get("file")
    s3 = boto3.resource(
        service_name='s3',
        region_name='us-east-1',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        aws_session_token=aws_session_token)  # for bucket in s3.buckets.all():
    # return bucket.name
    if avatar:
        avatar.save("%s/static/images/%s" % (app.root_path, avatar.filename))
    # return "SUCCESSFUL"
    # return "FAIL"
    s3.Bucket('rekognition3').upload_file("static/images/" + avatar.filename, avatar.filename)
    rekognitionImage = rekognition.detect_faces(avatar.filename, 'rekognition3')
    return render_template("rekognition_khuonmat.html", avatar=avatar.filename, rekog=rekognitionImage)


@app.route('/uploadbaoho', methods=['post'])
def upload_baoho():
    global aws_access_key_id
    global aws_secret_access_key
    global aws_session_token
    avatar = request.files.get("file")
    s3 = boto3.resource(
        service_name='s3',
        region_name='us-east-1',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        aws_session_token=aws_session_token)  # for bucket in s3.buckets.all():
    # return bucket.name
    if avatar:
        avatar.save("%s/static/images/%s" % (app.root_path, avatar.filename))
    # return "SUCCESSFUL"
    # return "FAIL"
    s3.Bucket('rekognition3').upload_file("static/images/" + avatar.filename, avatar.filename)
    A = rekognition.detect_baoho(avatar.filename, 'rekognition3')
    return render_template("rekognition_baoho.html", avatar=avatar.filename, A=A)


if __name__ == '__main__':
    app.run(debug=True)
