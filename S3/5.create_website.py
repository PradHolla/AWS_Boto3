import boto3

# s3 = boto3.client('s3')
# result = s3.get_bucket_website(Bucket='pradtest')

website_configuration = {
    'ErrorDocument': {'Key': 'error.html'},
    'IndexDocument': {'Suffix': 'index.html'},
}

# Set the website configuration
s3 = boto3.client('s3')
s3.put_bucket_website(Bucket='pradtest', WebsiteConfiguration=website_configuration)