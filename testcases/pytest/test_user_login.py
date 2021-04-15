from time import sleep

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestUserLogin(object):
    def setup_class(self):
        self.driver=webdriver.Chrome()
        self.driver.get('http://localhost:8080/jpress/user/login')
        self.driver.maximize_window()


    def test_user_login_username_error(self):
        username=''
        pwd='111111'
        expected='账号不能为空'


        self.driver.find_element_by_name('user').send_keys(username)

        self.driver.find_element_by_name('pwd').send_keys(pwd)

        self.driver.find_element_by_class_name('btn').click()


        WebDriverWait(self.driver,5).until(EC.alert_is_present())
        alert=self.driver.switch_to.alert
        sleep(3)

        assert alert.text ==expected

        alert.accept()

        # self.driver.quit()

    def test_user_login_ok(self):
        username = 'admin'
        pwd = '123456'
        expected = '用户中心'

        self.driver.find_element_by_name('user').clear()
        self.driver.find_element_by_name('user').send_keys(username)

        self.driver.find_element_by_name('pwd').clear()
        self.driver.find_element_by_name('pwd').send_keys(pwd)

        self.driver.find_element_by_class_name('btn').click()


        WebDriverWait(self.driver,5).until(EC.title_is(expected))

        sleep(3)

        assert self.driver.title==expected

        self.driver.quit()

