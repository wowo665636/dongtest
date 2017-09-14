import os
import unittest
from appium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from test.common.page import Page
from test.common.loginPage import login

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))


class ContactsAndroidTests(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1.2'
        desired_caps['deviceName'] = 'MI 3'
        # desired_caps['app'] = PATH('../../../sample-code/apps/ContactManager/ContactManager.apk')
        desired_caps['appPackage'] = 'com.palm.hubbiz'
        desired_caps['appActivity'] = 'com.palm.hubbiz.activity.IndexActivity'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test1(self):
        """
        locator_username = (By.ID, 'com.palm.hubbiz:id/login_username_et')
        locator_password = (By.ID, 'com.palm.hubbiz:id/login_password_et')
        locator_confirm = (By.ID, 'com.palm.hubbiz:id/login_confirm_btn')
        locator_find_passwd = (By.ID, 'com.palm.hubbiz: id / login_find_passwd')
        sleep(3)
        self.driver.find_element(*locator_username).send_keys('42010003')
        self.driver.find_element(*locator_password).send_keys('qqqqqq')
        self.driver.find_element(*locator_confirm).click()
        sleep(1)
        """
        self.driver.user_login()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ContactsAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
