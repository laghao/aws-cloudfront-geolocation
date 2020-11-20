import boto3, botocore, os, gzip, shutil
from configparser import ConfigParser
from datetime import date, timedelta

config = ConfigParser()
config.read('config.ini')

class CFNLogsClient:

    CFNLogBucket = (config['DEFAULT']['AWS_BUCKET_NAME'])
    Folder = (config['DEFAULT']['FOLDER'])
    Date = (config['DEFAULT']['DATE'])

    def __init__(self):
        self.log_files = []
        self.cfn_client = boto3.client('cloudfront')
        self.s3 = boto3.resource('s3')

    def main(self):
        self.get_s3_bucket_files()
        return self.extract_log_files()

    # TODO lookup Cloudfront log bucket directly
    def get_cloudfront_distribution(self):
        distributions = self.cfn_client.list_distributions()
        if distributions['DistributionList']['Quantity'] > 0:
            for distribution in distributions['DistributionList']['Items']:
                print("Domain: " + distribution['DomainName'])
                print("Distribution Id: " + distribution['Id'])
                print("Certificate Source: " + distribution['ViewerCertificate']['CertificateSource'])
                if (distribution['ViewerCertificate']['CertificateSource'] == "acm"):
                    print("Certificate: " + distribution['ViewerCertificate']['Certificate'])
                print("")
        else:    
            print("Error - No CloudFront Distributions Detected.") 

    def get_s3_bucket_files(self):
        log_bucket = self.s3.Bucket(self.CFNLogBucket).objects.all()
        if not os.path.exists(self.Folder):
            os.makedirs(self.Folder)
        for item in log_bucket:
            if not os.path.exists(self.Folder+(item.key).strip('.gz')+".log"):
                try:
                    obj = self.s3.Object(item.bucket_name, item.key)
                    if obj.last_modified.strftime('%Y%m%d') >= self.Date:
                        self.s3.Bucket(self.CFNLogBucket).download_file(item.key, self.Folder+item.key)
                except botocore.exceptions.ClientError as e:
                    if e.response['Error']['Code'] == "404":
                        print("The object does not exist.")
                    else:
                        raise
    
    def extract_log_files(self):
        for filename in os.listdir(os.getcwd()+"/"+self.Folder):
            if filename.endswith(".gz"):
                with gzip.open(os.path.join(os.getcwd(),self.Folder,filename), 'rb') as f_in:
                    with open(os.path.join(os.getcwd(),self.Folder,filename.strip('.gz')+".log"), 'wb') as f_out:
                        shutil.copyfileobj(f_in, f_out)
                if filename.endswith(".gz"):
                    os.remove(os.path.join((os.getcwd()+"/"+self.Folder),filename))
