from test.common.browser import Brower


class Page(Brower):
    def __init__(self, page=None, brower_type='firefox'):
        if page:
            self.driver = page.driver
        else:
            super(Page, self).__init__(brower_type=brower_type)

    def get_driver(self):
        return self.driver

    def find_element(self, *args):
        return self.driver.find_element(*args)

    def find_elements(self, *args):
        return self.driver.find_elements(*args)
