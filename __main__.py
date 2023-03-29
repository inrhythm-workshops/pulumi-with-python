from pulumi import export
from pulumi_aws import s3

web_bucket = s3.Bucket('s3-workshop-bucket')

# Export the name of the bucket
export('bucket_name', web_bucket.id)
