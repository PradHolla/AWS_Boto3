import boto3

# Delete the website configuration
s3 = boto3.client('s3')
s3.delete_bucket_website(Bucket='pradtest')