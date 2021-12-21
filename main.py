# from PIL import Image
import boto3
from flask import Flask, request, render_template
import rekognition

aws_access_key_id = "ASIAQYD45YXPM345ABNW"
aws_secret_access_key = "U8y+1ElqGtuUaKU17YxsnrYL7xzDfSwoHC8x9LkR"
aws_session_token = "FwoGZXIvYXdzEC4aDC/ufh+shNQJMPj2OCLKAd0ONa+phMRFvTqevLvMmvcAO9YGcnfTPZbrULBLxqwrX+S/zRRG4gJEe/zWVtdwbUwyKvudjUX5fCS0WSppebJZkkzIROq7XGgEttdIcl8RpPEwvjTnfz5XcD6ou8vFDtpetF0f1EBvTWNvV5qPCX/Koiqsa0vd/vzKHf7VNUKlB5l5l7lFBLrEIru6CReQxDCyfM3C9gzm8lmqath+T/3GD9kjC0KEWc+40DOYnINtPG4+qwaE5zkrax4WROUakJ8cwC84nhGPnNQosZuHjgYyLTbGeNReHAPz2V0ZG69ltTy32BxPwobg4wGmlrxJSLwr9CLqBxJ93V8sSZaEWA=="

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
