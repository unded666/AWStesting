import boto3
import numpy as np
import pandas as pd

# set up CLI according to AWS instructions.
# Create credentials file in ~/.aws/credentials (linux)
#                         in %PROFILE%/.aws/credentials (windows)
# credentials needs to contain:
#   [PROFILENAME]
#   aws_access_key_id
#   aws_secret_access_key
#   aws_session_token
#
#  PROFILENAME works easiest as "default", needs a bit of fiddling to work as othe forms...

FULL_URL = 's3://arcablanca-barchester-dcv-data-repo/full_dataset.csv'
BUCKET = 's3://arcablanca-barchester-dcv-data-repo/'
FILENAME = 'full_dataset.csv'

def
s3url = 's3://arcablanca-barchester-dcv-data-repo/full_dataset.csv'
print(s3url)
df = pd.read_csv(s3url)


if __name__ == '__main__':

    pass
