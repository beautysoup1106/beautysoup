import os

from PIL import Image
from selenium import webdriver
from time import sleep, time
import pytesseract

def test01():
    browser=webdriver.Chrome()

    browser.get('http://localhost:8080/jpress/user/register')
    browser.maximize_window()

    t=time()
    picture_name1=str(t)+'.png'
    browser.save_screenshot(picture_name1)

    ce=browser.find_element_by_id('captchaimg')

    left=ce.location['x']
    top=ce.location['y']
    right=ce.size['width']+left
    height=ce.size['height']+top

    dpr = browser.execute_script('return window.devicePixelRatio')

    im=Image.open(picture_name1)
    img=im.crop((left*dpr,top*dpr,right*dpr,height*dpr))

    t=time()
    picture_name2=str(t)+'.png'
    img.save(picture_name2)



def test02():

    image=Image.open('D:/workspace/my_selenium/test.png')


    str=pytesseract.image_to_string(image)
    print(str)
    print('22222')