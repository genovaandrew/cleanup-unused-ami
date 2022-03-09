# AWS Unused AMI Cleanup

## Prerequisites:

### Install boto3, and awscli:
```
pip install boto3
pip install awscli

# or
pip install -r requirements.txt
```

### Configure AWS with IAM account:
```
aws configure

AWS Access Key ID [None]: <YOUR_KEY_ID> 
AWS Secret Access Key [None]: <YOUR_SECRET_ACCESS_KEY>
Default region name [None]: us-east-1
Default output format [None]: json
```

### Then test the connection with a command like: 
```
aws sts get-caller-identity
```
## Script Usage:
```
usage: cleanup-unused-ami.py [-h] [-f]

options:
  -h, --help   show this help message and exit
  -f, --force  actually delete AMIs
```