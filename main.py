# from testcases.testcase01 import test02

from testcases.pytest.test_admin_login import TestAdminLogin
from testcases.pytest.test_article import TestArticle
if __name__ == '__main__':

    # driver=webdriver.Chrome()
    # driver.get('http://localhost:8080/jpress/user/register')
    # code=util.get_code(driver,'captchaimg')
    # print(code)
    # name=util.gen_random_str()
    # print(name)

    # case = TestUserLogin()
    # case.test_user_login_username_error()
    # case.test_user_login_ok()

    login =TestAdminLogin()
    # case.test_admin_login_code_error()
    login.test_admin_login_code_ok()
    # case = TestCatagory(login)
    # case.test_add_catagory_error()
    # case.test_add_catagory_ok()
    case=TestArticle(login)
    case.article_add_ok()
    case.article_one_delete_ok()
    #case.article_all_delete_ok()


