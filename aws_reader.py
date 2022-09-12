import boto3
import numpy as np
import pandas as pd

# set up CLI according to AWS instructions.
# Create credentials file in ~/.aws/credentials (linux)
#                         in %USERPROFILE%/.aws/credentials (windows)
# credentials needs to contain:
#   [PROFILENAME]
#   aws_access_key_id
#   aws_secret_access_key
#   aws_session_token
#
#  PROFILENAME works easiest as "default", needs a bit of fiddling to work as othe forms...

FULL_URL = 's3://arcablanca-barchester-dcv-data-repo/full_dataset.csv'
BUCKET = 'arcablanca-barchester-dcv-data-repo'
FILENAME = 'full_dataset.csv'
aws_access_key_id='ASIA447734G2JSAHJKUW'
aws_secret_access_key='Kxz4c28XzArSdhtial6r/fkU0w9Bipkk6Ua8lyLx'
aws_session_token='IQoJb3JpZ2luX2VjEPX//////////wEaCWV1LXdlc3QtMiJHMEUCIEmYJfTEEVAtOmmzcpXyUuvf8MeyDjbHqdAg5hi3ZsJbAiEA2ajQz7FFprpxkP+uCcgXwShCSd/c1O5negkva4RLdIAqiwMIjf//////////ARAAGgw4ODY5MTA0NzY3MjQiDGmYTyDIVeEVWpyy1yrfAry34H6Fg2D5/MQtK30En03CSfXvYFRv9TITJlqawzlURepUz1MvDri/p9EeMqpUiH1012ucGuZfrUS5NNWXODxqLGbXXQwTZ2AOEhIX+1qkG/b58sVT2QWOiLQfD6p1KPZF6LygbjAODFOUJN0VkfUF5ig+pPN8e8rPAbu9m4FSox3FIOGA8tyyLr29r221Izh8j4WOsdVyq+2hUoP2SzRRFHYqyli2wfkiM6FMBbpKmp6C7Y8b2GiRo9KjirBdaR1n6s+Sd8rN6Nc/ZHZk7bya7L0uEX/CawE+4cBhuClxSMPTKtJFvvYM0qw7uryBbLlU9fOCdZxurCYMnDVu1LVn2182x4Nz9uxlgwMUbe6dUvAHVhkeB7OAB4VQAhHwDj0CE2jhSbrsls5zxbbthrnyOSjnr0tLOFyt/h1Rxih0tkxlGw4SjZF3lJ5ttSvPhKuLIGPnBlizswJfxnDXdTCtxvyYBjqmAV77AK6FtG7TnVvAB6wlbHivTQQ2lgVPXMuH8ITOm7lakHs3ojUnOH2EldzzWsxdnLLb97m3KTRZ14L/9aPV/atyGxjf06jEeleFSLFGylNZq5yvl/cuKFB76ze3MTedzY/0fQjVm+KBldKhlYxhQXthbtoNX9+cpSyHurg4gOuQB8bkVrOZTVJLsRrv9fMviNmQWZA4nKVvcJkdQpo81S7IOJ/CuQU='

s3url = 's3://arcablanca-barchester-dcv-data-repo/full_dataset.csv'

def run_through_pandas():

    df = pd.read_csv(s3url)
    return df

def run_through_boto3():

    s3 = boto3.client('s3',
                      aws_access_key_id = aws_access_key_id,
                      aws_secret_access_key = aws_secret_access_key,
                      aws_session_token = aws_session_token)
    response = s3.get_object (Bucket = BUCKET,
                              Key = FILENAME)
    df = pd.read_csv(response.get("Body"))

    return df


if __name__ == '__main__':

    print(s3url)
    #df = run_through_pandas()
    df = run_through_boto3()

