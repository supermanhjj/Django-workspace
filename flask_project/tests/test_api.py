#coding:utf-8

import requests

# /img/upload_img
url = 'http://192.168.0.107:5000/img/upload_img'
files = {'file':("620644_14.jpg", open("C://Download//620644_14.jpg", "rb"),'image/jpg'), 'people_name':"xxx"}
r = requests.post(url, files=files)
result=r.text
print(result)