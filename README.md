
## Project spectrum

This is a python application which extracts IPs and Dates from AWS CLoudfront logs and adds gelocations to it.

The application takes following variables:

## Variables

### Default
REGION = eu-central-1 
FOLDER = files/
OUTPUT = output.list

### Required variables
AWS_BUCKET_NAME = 
AWS_ACCESS_KEY_ID = 
AWS_SECRET_ACCESS_KEY = 

## Deployment

```shell
$ docker run -e AWS_ACCESS_KEY_ID= AWS_SECRET_ACCESS_KEY= AWS_BUCKET_NAME= --name ip-exporter
```

