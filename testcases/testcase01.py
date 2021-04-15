from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains


def test01():
    print('test01')


def test02():
    driver=webdriver.Chrome()
    driver.get('http://www.jpress.io/user/register')
    elem=driver.find_element_by_id('agree')
    actions=ActionChains(driver)
    actions.move_to_element(elem).click().perform()

    sleep(3)