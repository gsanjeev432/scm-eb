import boto3
from django.conf import settings

class AWSManager:
    def __init__(self):
        self.sns_client = boto3.client('sns',
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            region_name=settings.AWS_REGION
        )
        
        self.sqs_client = boto3.client('sqs',
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            region_name=settings.AWS_REGION
        )
        
        self.s3_client = boto3.client('s3',
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            region_name=settings.AWS_REGION
        )

    def send_sns_notification(self, message, subject='Notification'):
        return self.sns_client.publish(
            TopicArn=settings.AWS_SNS_TOPIC_ARN,
            Message=message,
            Subject=subject
        )

    def send_sqs_message(self, message):
        return self.sqs_client.send_message(
            QueueUrl=settings.AWS_SQS_QUEUE_URL,
            MessageBody=message
        )

    def receive_sqs_messages(self, max_messages=10):
        return self.sqs_client.receive_message(
            QueueUrl=settings.AWS_SQS_QUEUE_URL,
            MaxNumberOfMessages=max_messages
        )

    def upload_file_to_s3(self, file_obj, file_name, content_type=None):
        extra_args = {'ACL': 'public-read'}
        if content_type:
            extra_args['ContentType'] = content_type
            
        self.s3_client.upload_fileobj(
            file_obj,
            settings.AWS_STORAGE_BUCKET_NAME,
            file_name,
            ExtraArgs=extra_args
        )
        return f"https://{settings.AWS_S3_CUSTOM_DOMAIN}/{file_name}" 