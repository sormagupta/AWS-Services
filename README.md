# Securely Serving Amazon S3 Content with Amazon CloudFront

This guide will walk you through the steps to serve content stored in an Amazon S3 bucket using Amazon CloudFront while ensuring secure and controlled access to your resources.

## Prerequisites

Before you begin, ensure you have the following prerequisites:

1. **AWS Account**: You should have an AWS account. If you don't have one, you can [create an AWS account](https://aws.amazon.com/free/).

2. **Amazon S3 Bucket**: Create an Amazon S3 bucket to store your content. Make sure your content is uploaded to this bucket.

3. **Amazon CloudFront Distribution**: Set up an Amazon CloudFront distribution that will serve your S3 content. Make a note of the CloudFront distribution domain name.

4. **Access Control**: Decide on your desired access control method for the content. You can choose to make the content public, restrict access to specific users, or use signed URLs or cookies for secure access.

## Secure Access Methods

### 1. Public Content

If your content is intended to be publicly accessible, configure your CloudFront distribution with a default behavior that allows public access to your S3 bucket.

### 3. Signed URLs

Signed URLs provide time-limited access to your content. To generate signed URLs, you can use AWS SDKs, CLI, or code snippets in various programming languages. Here's an example using Python:

### 3. Generate public and private key

openssl genrsa -out private_key.pem 2048
openssl rsa -pubout -in private_key.pem -out public_key.pem
