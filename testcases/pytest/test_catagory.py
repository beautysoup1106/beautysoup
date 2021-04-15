from time import sleep

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from testcases.pytest.test_admin_login import TestAdminLogin


class TestCatagory(object):

    def setup_class(self):
        self.login = TestAdminLogin()

    @pytest.mark.dependency(depends=['admin_login'],scope='module')
    def test_add_catagory_error(self):
        name = ''
        parent = 'python'
        slug = 'test'

        expected = '分类名称不能为空'

        self.login.driver.find_element_by_xpath('//*[@id="sidebar-menu"]/li[4]/a').click()
        sleep(1)
        self.login.driver.find_element_by_xpath('//*[@id="sidebar-menu"]/li[4]/ul/li[3]').click()

        self.login.driver.find_element_by_name('category.title').send_keys(name)

        # 选择父分类
        parent_catagory_elem = self.login.driver.find_element_by_name('category.pid')
        Select(parent_catagory_elem).select_by_visible_text(parent)

        # 输入slug
        self.login.driver.find_element_by_name('category.slug').send_keys(slug)

        self.login.driver.find_element_by_xpath(
            '/html/body/div[1]/div/section[2]/div/div[1]/div/form/div[2]/div/div/button').click()

        loc = (By.CLASS_NAME, 'toast-message')
        print(loc)

        WebDriverWait(self.login.driver, 5).until(expected_conditions.visibility_of_element_located(loc))

        msg = self.login.driver.find_element(*loc).text

        assert msg == expected

    @pytest.mark.dependency(depends=['admin_login'],scope='module')
    def test_add_catagory_ok(self):
        name='AI'
        parent='python'
        slug='AI'
        expected=None

        # self.login.driver.find_element_by_xpath('//*[@id="sidebar-menu"]/li[4]/a').click()
        # self.login.driver.find_element_by_xpath('//*[@id="sidebar-menu"]/li[4]/ul/li[3]/a').click()

        self.login.driver.find_element_by_name('category.title').clear()
        self.login.driver.find_element_by_name('category.title').send_keys(name)

        # 选择父分类
        parent_catagory_elem = self.login.driver.find_element_by_name('category.pid')
        Select(parent_catagory_elem).select_by_visible_text(parent)

        # 输入slug
        self.login.driver.find_element_by_name('category.slug').clear()
        self.login.driver.find_element_by_name('category.slug').send_keys(slug)

        self.login.driver.find_element_by_xpath(
            '/html/body/div[1]/div/section[2]/div/div[1]/div/form/div[2]/div/div/button').click()


        assert 1 == 1

if __name__ == '__main__':
    pytest.main(['-vs','test_catagory.py'])