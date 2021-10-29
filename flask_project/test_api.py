#coding:utf-8

import requests
url = 'http://192.168.3.16:5000/img/upload_img'
files = {'file':("620644_14.jpg", open("C://Download//620644_14.jpg", "rb"),'image/jpg'), 'people_name':"sjjj"}
r = requests.post(url, files=files)
result=r.text
print(result)