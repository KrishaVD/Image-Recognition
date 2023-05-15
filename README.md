# Image-Recognition
Image analysis using amazon Rekognition 


**Introduction**

AWS offers a robust suite of cloud services that can power nearly any application requirement. In this tutorial, we'll use AWS S3, Lambda, Rekognition and SNS.

Our goal is to create an automated process that kicks off when an image is uploaded to an S3 bucket. This triggers a Lambda function which uses Rekognition to analyse the image, identifying objects and scenes. The results of this analysis are then published to an SNS topic, sending an email notification with the results. 

**Technologies Used**

•	Amazon S3 (Simple Storage Service): This is an object storage service that offers industry-leading scalability, data availability, security, and performance. In this project, it's used as the starting point of our process, storing the images that are to be analysed.

•	AWS Lambda: It's a serverless compute service that runs your code in response to events and automatically manages the underlying compute resources for you. In this project, AWS Lambda functions are triggered when an image is uploaded to S3, carrying out the image analysis using Rekognition.

•	Amazon Rekognition: This is a cloud-based image and video analysis service that can identify objects, people, text, scenes, and activities, as well as detect any inappropriate content. In this project, it's used to analyse the images uploaded to S3.

•	Amazon SNS (Simple Notification Service): It's a web service that coordinates and manages the delivery or sending of messages to subscribing endpoints or clients. In this project, SNS is used to send out an email notification that contains the results of the image analysis.
Project Setup

You can access the complete project on GitHub at `https://github.com/KrishaVD/Image-Recognition.git`. Here are the steps you can follow to set up and run the project locally.


**Prerequisites**

•	Before you begin, you'll need an AWS account. You can sign up for a free tier account (https://aws.amazon.com/free/).
•	Basic knowledge of AWS services like Lambda, API Gateway, and Comprehend.
•	Basic understanding of HTML/CSS/JavaScript.


**Setup Instructions**

Step 1: Setting up the S3 Bucket
First, we need a place to store our images. AWS S3 (Simple Storage Service) is perfect for this. Once you're logged into the AWS Management Console, navigate to the S3 service and create a new bucket. You can name it whatever you like – we'll call ours "rekognition-bucket".

Step 2: Creating the Lambda Function

AWS Lambda is a service that lets you run code without provisioning or managing servers. We'll use Lambda to analyse our images with Rekognition whenever a new image is uploaded to our S3 bucket.
Navigate to the Lambda service in the AWS Console and create a new function. You can name it "rekognition-function". In the function code, paste in the Python code from this [GitHub repository] (https://github.com/my-repo/rekognition-function). This function will be triggered by an event from our S3 bucket.
Remember to replace the bucket name in the code with the name of your own bucket, and adjust the `MaxLabels` parameter as you see fit. This parameter determines how many labels (i.e., objects or scenes) Rekognition will attempt to identify in each image.


Step 3: Creating the SNS Topic

AWS SNS (Simple Notification Service) is a flexible, fully-managed pub/sub messaging and mobile notifications service for coordinating the delivery of messages to subscribing endpoints and clients. We'll use SNS to send ourselves an email whenever our Lambda function has finished analysing an image.
In the SNS service, create a new topic and call it "rekognition-topic". Next, create a subscription for your topic. The protocol should be "Email", and the endpoint should be the email address where you want to receive the notifications.

**Conclusion**

This project demonstrates the powerful capabilities of AWS services to create an automated image analysis system. By harnessing the strengths of S3, Lambda, Rekognition, and SNS, we've established a pipeline that can autonomously analyse images, identify objects or scenes, and alert us via email of the results. This setup can be incredibly useful in various scenarios, such as moderating content, cataloging digital assets, or even supporting machine learning projects. You can further customize and expand this system as per your needs, maybe by integrating more AWS services or tweaking the existing ones.

Happy exploring with AWS!
