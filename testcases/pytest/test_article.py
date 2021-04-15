from time import sleep

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from testcases.pytest.test_admin_login import TestAdminLogin


class TestArticle(object):

    def setup_class(self):
        self.login = TestAdminLogin()


    @pytest.mark.dependency(depends=['admin_login'],scope='module')
    def article_add_ok(self):
        title = '我的文章1'
        content = '我的文章内容1'
        expected = '文章保存成功。'

        self.login.driver.find_element_by_xpath('//*[@id="sidebar-menu"]/li[4]/a').click()
        sleep(1)
        self.login.driver.find_element_by_xpath('//*[@id="sidebar-menu"]/li[4]/ul/li[1]/a').click()
        sleep(1)
        self.login.driver.find_element_by_xpath('/html/body/div[1]/div/section[3]/div/div/div/div[1]/div/div/a').click()
        sleep(1)

        #self.login.driver.find_element_by_id('article-title').clear()
        self.login.driver.find_element_by_id('article-title').send_keys(title)

        iframe = self.login.driver.find_element_by_xpath('//*[@id="cke_1_contents"]/iframe')

        self.login.driver.switch_to.frame(iframe)
        sleep(1)

        #self.login.driver.find_element_by_xpath('/html/body/p').clear()
        self.login.driver.find_element_by_xpath('/html/body/p').send_keys(content)

        self.login.driver.switch_to.default_content()

        self.login.driver.find_element_by_xpath('//*[@id="form"]/div/div[2]/div[1]/div/button[1]').click()

        loc = (By.CLASS_NAME, 'toast-message')
        WebDriverWait(self.login.driver, 5).until(expected_conditions.visibility_of_element_located(loc))

        msg = self.login.driver.find_element(*loc).text

        assert msg == expected


    @pytest.mark.dependency(depends=['admin_login'],scope='module')
    def article_one_delete_ok(self):
        self.login.driver.find_element_by_xpath('//*[@id="sidebar-menu"]/li[4]/ul/li[1]/a').click()
        sleep(1)

        link = self.login.driver.find_element_by_xpath(
            '/html/body/div[1]/div/section[3]/div/div/div/div[2]/table/tbody/tr[2]/td[2]/strong')

        ActionChains(self.login.driver).move_to_element(link).perform()

        num = len(self.login.driver.find_elements_by_class_name('jp-actiontr'))
        print(num)

        self.login.driver.find_element_by_xpath(
            '/html/body/div[1]/div/section[3]/div/div/div/div[2]/table/tbody/tr[2]/td[2]/div/div/a[3]').click()
        sleep(5)
        num2 = len(self.login.driver.find_elements_by_class_name('jp-actiontr'))
        print(num2)

       # assert num == num2 + 1


    @pytest.mark.dependency(depends=['admin_login'],scope='module')
    def article_all_delete_ok(self):

        self.login.driver.find_element_by_xpath('/html/body/div[1]/div/section[3]/div/div/div/div[2]/table/tbody/tr[1]/th[1]/input').click()
        self.login.driver.find_element_by_id('batchDel').click()

        WebDriverWait(self.login.driver,5).until(expected_conditions.alert_is_present())
        alert=self.login.driver.switch_to.alert
        alert.accept()



        # num = len(self.login.driver.find_elements_by_class_name('jp-actiontr'))



if __name__ == '__main__':
    pytest.main(['-vs','test_article.py'])

