import boto3

def detect_labels(photo, bucket):

    client = boto3.client(service_name='rekognition',
                          region_name='us-east-1',
                          aws_access_key_id='ASIA3MNQVSTPJABNQLPK',
                          aws_secret_access_key='1L263MFr0/Xu/v6joqyT3MqqdYlD2HgbVBkZzpnD',
                          aws_session_token='FwoGZXIvYXdzECwaDBBCl9giZWjx1HOZUyLPAR/U7lm0CD3HTqz2JO0JPnasnbshXPoC5W+qktYiXGCBRwmYxh7p/g6x/j3xrwLqstOKJ4HXc2YriE7gnVx9OIr8n+hIBa2gneC09lj5qo5z6fyvfsa6onec0xuY6xk8ldD9eWetrhfEY2YTRhcLhFgcJT2NSz9Y1o3pgVRbasae7ZgS2qiWX687TK5Kkk+dOifskT21dc6WVnA2aJu+IkOVqAEbyaB6S6SUnkTiJimzenNEU0vaozTW6K23TzQrK9Lpj8wZ5W+SAFlx4JKF0SjF+N2MBjIt3ucSkstNrs0GKp/cYWLfDR8ydyioUAb3TMOaOl5jbVS1Loa65PDbq/0H8WrW')

    response = client.detect_labels(Image={'S3Object': {'Bucket': bucket, 'Name': photo}}, MaxLabels=10)
    value = ""
    value = value + '\nDetected labels for' + photo
    for label in response['Labels']:
        value = value + '\nLabel: ' + label['Name']
        value = value + '\nConfidence: ' + str(label['Confidence'])
        value = value + '\nInstances:'
        for instance in label['Instances']:
            value = value + '\nBounding box'
            value = value + '\nTop: ' + str(instance['BoundingBox']['Top'])
            value = value + '\nLeft: ' + str(instance['BoundingBox']['Left'])
            value = value + '\nWidth: ' + str(instance['BoundingBox']['Width'])
            value = value + '\nHeight: ' + str(instance['BoundingBox']['Height'])
            value = value + '\nConfidence: ' + str(instance['Confidence'])

        value = value + '\nParents:'
        for parent in label['Parents']:
            value = value + "   " + parent['Name']

        value = value + "----------"
        value = value + str(len(response['Labels']))
    return value