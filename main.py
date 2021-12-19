import os
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import rekognition


#from PIL import Image
import boto3


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
	avatar = request.files.get("file")
	s3 = boto3.resource(
		service_name='s3',
		region_name='us-east-1',
		aws_access_key_id='ASIAQYD45YXPGR6QR2NT',
		aws_secret_access_key='Gzz3FpTy37cIvkmhggEp+f4bjpbPQbJ/axzyE632',
		aws_session_token='FwoGZXIvYXdzEP3//////////wEaDHxYdOQffhjKTVUiKCLKAUbirUiSQyBVSrF0YRt1iw/svvSzeQVqXXrawLukqiOvdlu/IVIYokqF0YhA3OPD8s8ZM4iPVnbWjNDor86oFbYefu18F99Lx/kcmYOw1BK9ip7CesQMvK/DpS7WHyDuooZquzfaGWD/CaqYNOIy1v4Dj37G7TBjAixWz2THRvGNY/UbdJMapK0SLYxsfpd0vI2oz0SNZZMe6BgQN+zTdPAx6gpp991828fav866W3ROWY1i4e3BERXrprWnipuNm1kKd2MoCTWbTgMo4bv8jQYyLX6HrjSkoxObrGvJykJxwAx+CgtoYFc8Megui4Nhmykl9Lu75YCR5xhgx3SUGA==')
	#for bucket in s3.buckets.all():
		#return bucket.name
	if avatar:
		avatar.save("%s/static/images/%s" % (app.root_path, avatar.filename))
		#return "SUCCESSFUL"
	#return "FAIL"
	s3.Bucket('rekognition3').upload_file("static/images/"+avatar.filename, avatar.filename)
	rekognitionImage = rekognition.detect_labels(avatar.filename, 'rekognition3')
	return render_template("rekognition_object.html", avatar=avatar.filename, rekog=rekognitionImage)


@app.route('/uploadkhuonmat', methods=['post'])
def upload_km():
	avatar = request.files.get("file")
	s3 = boto3.resource(
		service_name='s3',
		region_name='us-east-1',
		aws_access_key_id='ASIAQYD45YXPGR6QR2NT',
		aws_secret_access_key='Gzz3FpTy37cIvkmhggEp+f4bjpbPQbJ/axzyE632',
		aws_session_token='FwoGZXIvYXdzEP3//////////wEaDHxYdOQffhjKTVUiKCLKAUbirUiSQyBVSrF0YRt1iw/svvSzeQVqXXrawLukqiOvdlu/IVIYokqF0YhA3OPD8s8ZM4iPVnbWjNDor86oFbYefu18F99Lx/kcmYOw1BK9ip7CesQMvK/DpS7WHyDuooZquzfaGWD/CaqYNOIy1v4Dj37G7TBjAixWz2THRvGNY/UbdJMapK0SLYxsfpd0vI2oz0SNZZMe6BgQN+zTdPAx6gpp991828fav866W3ROWY1i4e3BERXrprWnipuNm1kKd2MoCTWbTgMo4bv8jQYyLX6HrjSkoxObrGvJykJxwAx+CgtoYFc8Megui4Nhmykl9Lu75YCR5xhgx3SUGA==')
	#for bucket in s3.buckets.all():
		#return bucket.name
	if avatar:
		avatar.save("%s/static/images/%s" % (app.root_path, avatar.filename))
		#return "SUCCESSFUL"
	#return "FAIL"
	s3.Bucket('rekognition3').upload_file("static/images/"+avatar.filename, avatar.filename)
	rekognitionImage = rekognition.detect_faces(avatar.filename, 'rekognition3')
	return render_template("rekognition_khuonmat.html", avatar=avatar.filename, rekog=rekognitionImage)


@app.route('/uploadbaoho', methods=['post'])
def upload_baoho():
	avatar = request.files.get("file")
	s3 = boto3.resource(
		service_name='s3',
		region_name='us-east-1',
		aws_access_key_id='ASIAQYD45YXPGR6QR2NT',
		aws_secret_access_key='Gzz3FpTy37cIvkmhggEp+f4bjpbPQbJ/axzyE632',
		aws_session_token='FwoGZXIvYXdzEP3//////////wEaDHxYdOQffhjKTVUiKCLKAUbirUiSQyBVSrF0YRt1iw/svvSzeQVqXXrawLukqiOvdlu/IVIYokqF0YhA3OPD8s8ZM4iPVnbWjNDor86oFbYefu18F99Lx/kcmYOw1BK9ip7CesQMvK/DpS7WHyDuooZquzfaGWD/CaqYNOIy1v4Dj37G7TBjAixWz2THRvGNY/UbdJMapK0SLYxsfpd0vI2oz0SNZZMe6BgQN+zTdPAx6gpp991828fav866W3ROWY1i4e3BERXrprWnipuNm1kKd2MoCTWbTgMo4bv8jQYyLX6HrjSkoxObrGvJykJxwAx+CgtoYFc8Megui4Nhmykl9Lu75YCR5xhgx3SUGA==')
	#for bucket in s3.buckets.all():
		#return bucket.name
	if avatar:
		avatar.save("%s/static/images/%s" % (app.root_path, avatar.filename))
		#return "SUCCESSFUL"
	#return "FAIL"
	s3.Bucket('rekognition3').upload_file("static/images/"+avatar.filename, avatar.filename)
	A= rekognition.detect_baoho(avatar.filename, 'rekognition3')
	return render_template("rekognition_baoho.html", avatar=avatar.filename, A=A)



#@app.route('/', methods=['POST'])
#def upload_video():
#	if 'file' not in request.files:
#		flash('No file part')
#		return redirect(request.url)
#	file = request.files['file']
#	if file.filename == '':
#		flash('No image selected for uploading')
#		return redirect(request.url)
#	else:
#		filename = secure_filename(file.filename)
#		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		#print('upload_video filename: ' + filename)
#		flash('Video successfully uploaded and displayed below')
#		return render_template('home.html', filename=filename)

#@app.route('/display/<filename>')
#def display_video(filename):
#	#print('display_video filename: ' + filename)
#	return redirect(url_for('static', filename='uploads/' + filename), code=301)


if __name__ == '__main__':
    app.run(debug=True)
