# encoding:utf-8

import requests
import base64

'''
植物识别
'''

request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/plant"
# 二进制方式打开图片文件
f = open('/Users/zhiquanxu/Desktop/e5ce636b5ce83fc32510fa7521ed61.jpg', 'rb')
img = base64.b64encode(f.read())

params = {"image":img}
access_token = '24.19d536e7cc44f4bb1ff673454fec0644.2592000.1682822499.282335-31846426'
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print (response.json())