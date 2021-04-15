from time import sleep

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest
from util import util


class TestAdminLogin(object):
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:8080/jpress/admin/login')
        self.driver.maximize_window()

    # 测试管理员登录验证码错误
    def test_admin_login_code_error(self):
        username = 'admin'
        pwd = '123456'
        captcha = '666'
        expected = '验证码不正确，请重新输入'

        self.driver.find_element_by_name('user').send_keys(username)
        self.driver.find_element_by_name('pwd').send_keys(pwd)
        self.driver.find_element_by_name('captcha').send_keys(captcha)
        self.driver.find_element_by_class_name('btn').click()

        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert

        assert alert.text == expected
        alert.accept()
        sleep(5)
    @pytest.mark.dependency(name='admin_login')
    def test_admin_login_code_ok(self):
        username = 'admin'
        pwd = '123456'
        expected = 'JPress后台'

        self.driver.find_element_by_name('user').clear()
        self.driver.find_element_by_name('user').send_keys(username)

        self.driver.find_element_by_name('pwd').clear()
        self.driver.find_element_by_name('pwd').send_keys(pwd)

        captcha = util.get_code(self.driver, 'captchaImg')

        self.driver.find_element_by_name('captcha').clear()
        self.driver.find_element_by_name('captcha').send_keys(captcha)

        self.driver.find_element_by_class_name('btn').click()

        print(EC.title_is(expected))
        WebDriverWait(self.driver, 5).until(EC.title_is(expected))

        assert expected == self.driver.title

        sleep(5)

        # self.driver.quit()

if __name__ == '__main__':
    pytest.main(['-vs','test_admin_login.py'])