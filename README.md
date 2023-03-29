[![Deploy](https://get.pulumi.com/new/button.svg)](https://app.pulumi.com/new?template=https://github.com/pulumi/examples/blob/master/aws-py-s3-folder/README.md)

# Host a Static Website on Amazon S3

A static website that uses [S3's website support](https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html).
For a detailed walkthrough of this example, see the tutorial [Static Website on AWS S3](https://www.pulumi.com/docs/tutorials/aws/s3-website/).

## Prerequisites
Before we begin, make sure you have the following:

|Name|Version|Notes|
|----|-------|-----|
|[Python](https://www.python.org/downloads/)|3.7 or greater | 3.11.2 is recommended and used for this demo|
|[Pulumi](https://www.pulumi.com/docs/get-started/install/)|3.60.0|This is the version being used for this demo|
|AWS keys||Credentials should have been provided prior. Please reach out if you have not received yours|

## Deploying and running the program

Note: some values in this example will be different from run to run.  These values are indicated
with `***`.

1. Create a new stack:

    ```bash
    $ pulumi stack init dev
    ```

1. Set the AWS region:

    ```bash
    $ pulumi config set aws:region us-east-1
    ```

1. Run `pulumi up` to preview and deploy changes.  After the preview is shown you will be
    prompted if you want to continue or not.

    ```bash
    $ pulumi up
    Previewing update (dev):

        Type                    Name                  Plan       
    +   pulumi:pulumi:Stack     aws-py-s3-folder-dev  create     
    +   ├─ aws:s3:Bucket        s3-workshop-bucket     create     
    +   ├─ aws:s3:BucketObject  index.html            create     
    +   ├─ aws:s3:BucketObject  python.png            create     
    +   ├─ aws:s3:BucketObject  favicon.png           create     
    +   └─ aws:s3:BucketPolicy  bucket-policy         create     

    Resources:
        + 6 to create

    Do you want to perform this update?
    > yes
      no
      details
    ```

1. To see the resources that were created, run `pulumi stack output`:

    ```bash
    $ pulumi stack output
    Current stack outputs (2):
        OUTPUT                                           VALUE
        bucket_name                                      s3-workshop-bucket-***
        website_url                                      ***.s3-website-us-east-1.amazonaws.com
    ```

1. To see that the S3 objects exist, you can either use the AWS Console or the AWS CLI:

    ```bash
    $ aws s3 ls $(pulumi stack output bucket_name)
    2018-04-17 15:40:47      13731 favicon.png
    2018-04-17 15:40:48        249 index.html
    ```

1. Open the site URL in a browser to see both the rendered HTML, the favicon, and Python splash image:

    ```bash
    $ pulumi stack output website_url
    ***.s3-website-us-west-2.amazonaws.com
    ```

1. To clean up resources, run `pulumi destroy` and answer the confirmation question at the prompt.
