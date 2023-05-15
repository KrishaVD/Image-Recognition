import json
import boto3
import urllib

def lambda_handler(event, context):
    rekognition = boto3.client('rekognition')
    s3 = boto3.client('s3')
    sns = boto3.client('sns')
    

    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding ='utf-8')
    
    # Call Rekognition API
    response = rekognition.detect_labels (Image = {"S3Object": {"Bucket":bucket, "Name": key }}, MaxLabels=3)
    
    # Extract the labels and confidence levels, round confidence to two decimal places
    labels_confidences = [f"Name: {label['Name']}, Confidence: {round(label['Confidence'], 2)}" for label in response['Labels']]
    
    # Convert the extracted data to a formatted string
    tosend = '\n'.join(labels_confidences)
    print(tosend)
    
    # Form a subject string
    subject_str = 'Uploaded Image Labels for ' + key
    
    # Publish the response to SNS
    message = sns.publish(
        TargetArn='arn:aws:sns:us-east-1:741606613310:image-rekognition',
        Message=tosend,
        Subject=subject_str
    )

    
    return {
        'statusCode': 200,
        'body': json.dumps('Image processed successfully!')
    }
