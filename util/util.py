import base64
import json
import os
import pickle
import random
import string
import time
import urllib
import urllib.request

from PIL import Image


def get_code(driver, id):

    t=time.time()
    path=os.path.dirname(os.path.dirname(__file__))+'/screenshots'

    picture_name1=path+'/'+str(t)+'.png'

    driver.save_screenshot(picture_name1)

    ce=driver.find_element_by_id(id)

    left=ce.location['x']
    top=ce.location['y']
    right=ce.size['width']+left
    height=ce.size['height']+top

    drp=driver.execute_script('return window.devicePixelRatio')

    im=Image.open(picture_name1)

    img=im.crop((left*drp,top*drp,right*drp,height*drp))

    t=time.time()

    picture_name2=path+'/'+str(t)+'.png'
    img.save(picture_name2)

    # API产品路径
    host = 'https://codevirify.market.alicloudapi.com'
    path = '/icredit_ai_image/verify_code/v1'
    # 阿里云APPCODE
    appcode = '07d9d34fea414e13961f5d792cc41522'
    url = host + path
    bodys = {}
    querys = ""

    # 启用BASE64编码方式进行识别
    # 内容数据类型是BASE64编码
    f = open(picture_name2, 'rb')
    contents = base64.b64encode(f.read())
    f.close()
    bodys['IMAGE'] = contents
    bodys['IMAGE_TYPE'] = '0'

    post_data = urllib.parse.urlencode(bodys).encode('utf-8')

    request = urllib.request.Request(url, post_data)
    request.add_header('Authorization', 'APPCODE ' + appcode)
    request.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
    response = urllib.request.urlopen(request)
    content = response.read()
    if (content):
        res=json.loads(content.decode('utf-8'))
        return res['VERIFY_CODE_ENTITY']['VERIFY_CODE']

#生成随机字符串
def gen_random_str():
    rand_str=''.join(random.sample(string.ascii_letters+string.digits,8))

    return rand_str

def save_cookie(driver,path):
    with open(path,'wb') as filehandler:
        cookies=driver.get_cookies()
        print(cookies)
        pickle.dump(cookies,filehandler)


def load_cookie(driver,path):
    with open(path, 'rb') as cookiesfile:
        cookies=pickle.load(cookiesfile)
        for cookie in cookies:
            driver.add_cookie(cookie)








