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
	return render_template('upload_image.html')


@app.route('/upload', methods=['post'])
def upload():
	avatar = request.files.get("file")
	s3 = boto3.resource(
		service_name='s3',
		region_name='us-east-1',
		aws_access_key_id='ASIA3MNQVSTPJABNQLPK',
		aws_secret_access_key='1L263MFr0/Xu/v6joqyT3MqqdYlD2HgbVBkZzpnD',
		aws_session_token='FwoGZXIvYXdzECwaDBBCl9giZWjx1HOZUyLPAR/U7lm0CD3HTqz2JO0JPnasnbshXPoC5W+qktYiXGCBRwmYxh7p/g6x/j3xrwLqstOKJ4HXc2YriE7gnVx9OIr8n+hIBa2gneC09lj5qo5z6fyvfsa6onec0xuY6xk8ldD9eWetrhfEY2YTRhcLhFgcJT2NSz9Y1o3pgVRbasae7ZgS2qiWX687TK5Kkk+dOifskT21dc6WVnA2aJu+IkOVqAEbyaB6S6SUnkTiJimzenNEU0vaozTW6K23TzQrK9Lpj8wZ5W+SAFlx4JKF0SjF+N2MBjIt3ucSkstNrs0GKp/cYWLfDR8ydyioUAb3TMOaOl5jbVS1Loa65PDbq/0H8WrW')
	#for bucket in s3.buckets.all():
		#return bucket.name
	if avatar:
		avatar.save("%s/static/images/%s" % (app.root_path, avatar.filename))
		#return "SUCCESSFUL"
	#return "FAIL"
	s3.Bucket('rekognition1').upload_file("static/images/"+avatar.filename, avatar.filename)
	rekognitionImage = rekognition.detect_labels(avatar.filename, 'rekognition1')
	return render_template("rekognition.html", avatar=avatar.filename, rekog=rekognitionImage)

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