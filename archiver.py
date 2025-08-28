import os
import datetime
import shutil

dt_now = datetime.datetime.now()
year = str(dt_now.year)

if(dt_now.month>10):
    month = str(dt_now.month)
else:
    month = "0" + str(dt_now.month)

if(dt_now.day>10):
    day = str(dt_now.day)
else:
    day = "0" + str(dt_now.day)

foldername = year + "-" + month + "-" + day

dir_path ='archive/' + foldername
if(os.path.exists(dir_path) == False):
    os.mkdir(dir_path)

filename = 'test.py'

shutil.copy('main.py',dir_path + "/" + filename)

print("success!")