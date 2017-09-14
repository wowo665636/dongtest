from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from test.common.page import Page


class login(Page):
    """
    用户登录界面
    """

    # Action进入到登录页面
    locator_username = (By.ID, 'com.palm.hubbiz:id/login_username_et')
    locator_password = (By.ID, 'com.palm.hubbiz:id/login_password_et')
    locator_confirm = (By.ID, 'com.palm.hubbiz:id/login_confirm_btn')
    locator_find_passwd = (By.ID, 'com.palm.hubbiz: id / login_find_passwd')

    # 登录用户名
    def login_username(self, username):
        self.driver.find_element(*self.locator_username).send_keys(username)

    # 登录密码
    def login_password(self, password):
        self.driver.find_element(*self.locator_password).send_keys(password)


    # 定义统一登录入口
    def user_login(self, username='42010003', password='qqqqqq'):
        """获取的用户名密码登录"""
        sleep(3)
        self.login_username(username)
        self.login_password(password)
        self.driver.find_element(*self.locator_confirm).click()
        sleep(1)
