from selenium.webdriver.support import expected_conditions as EC


from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from util import util


class TestUserRegister(object):
    def setup_class(self):
        self.driver=webdriver.Chrome()
        self.driver.get('http://localhost:8080/jpress/user/register')
        self.driver.maximize_window()

    #测试登录验证码错误
    def test_register_code_error(self):
        username='test-001'
        email='test-001@qq.com'
        pwd='111111'
        confirmPwd='111111'
        captcha='aaa'
        expected='验证码不正确'

        self.driver.find_element_by_name('username').send_keys(username)
        self.driver.find_element_by_name("email").send_keys(email)

        self.driver.find_element_by_name('pwd').send_keys(pwd)
        self.driver.find_element_by_name('confirmPwd').send_keys(confirmPwd)

        self.driver.find_element_by_name('captcha').send_keys(captcha)
        self.driver.find_element_by_class_name('btn').click()

        WebDriverWait(self.driver,5).until(EC.alert_is_present())
        alert=self.driver.switch_to.alert

        assert alert.text == expected

        alert.accept()


    def test_register_ok(self):
        username = util.gen_random_str()
        email = username+'@qq.com'
        pwd = '111111'
        confirmPwd = '111111'
        captcha = ''
        expected = '注册成功，点击确定进行登录。'


        self.driver.find_element_by_name('username').clear()
        self.driver.find_element_by_name('username').send_keys(username)

        self.driver.find_element_by_name("email").clear()
        self.driver.find_element_by_name("email").send_keys(email)

        self.driver.find_element_by_name('pwd').clear()
        self.driver.find_element_by_name('pwd').send_keys(pwd)

        self.driver.find_element_by_name('confirmPwd').clear()
        self.driver.find_element_by_name('confirmPwd').send_keys(confirmPwd)

        self.driver.find_element_by_name('captcha').clear()

        captcha=util.get_code(self.driver,'captchaimg')
        self.driver.find_element_by_name('captcha').send_keys(captcha)
        self.driver.find_element_by_class_name('btn').click()

        WebDriverWait(self.driver,5).until(EC.alert_is_present())
        alert=self.driver.switch_to.alert

        assert alert.text == expected

        alert.accept()
