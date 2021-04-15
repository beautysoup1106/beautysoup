# from lib.ShowapiRequest import ShowapiRequest
#
# r = ShowapiRequest("http://route.showapi.com/2360-1","579492","448ce21f72204815876f8557a7693223" )
# r.addBodyPara("img_url", "D:/workspace/my_selenium/test.png")
# res = r.post()
# print(res.text)


# -*- coding: UTF-8 -*-
# !/usr/bin/python3
# 版权所有 © 艾科瑞特科技
# 艾科瑞特（iCREDIT）-让企业业绩长青
# 预知更多业绩长青，请与我们联系
# 联系电话：0532-88984128
# 联系邮箱：market@itruth.xin

import urllib
import urllib.request
import base64
import re

#API产品路径
host = 'https://codevirify.market.alicloudapi.com'
path = '/icredit_ai_image/verify_code/v1'
#阿里云APPCODE
appcode = '07d9d34fea414e13961f5d792cc41522'
url = host + path
bodys = {}
querys = ""

#参数配置
if True:
    #启用BASE64编码方式进行识别
    #内容数据类型是BASE64编码
    f = open(r'D:/workspace/my_selenium/1616644061.8829603.png', 'rb')
    contents = base64.b64encode(f.read())
    f.close()
    bodys['IMAGE'] = contents
    bodys['IMAGE_TYPE'] = '0'
else:
    #启用URL方式进行识别
    #内容数据类型是图像文件URL链接
    bodys['IMAGE'] = 'D:/workspace/my_selenium/1616644061.8829603.png'
    bodys['IMAGE_TYPE'] = '1'

post_data = urllib.parse.urlencode(bodys).encode('utf-8')

request = urllib.request.Request(url, post_data)
request.add_header('Authorization', 'APPCODE ' + appcode)
request.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
response = urllib.request.urlopen(request)
content = response.read()
if (content):
    print(content.decode('utf-8'))