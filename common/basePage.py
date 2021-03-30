from logging import Logger

from selenium import webdriver

from selenium.common.exceptions import NoSuchElementException


# logger = Logger(logger='BasePage').getlog()
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage():
    _driver = None
    _base_url="http://172.16.201.60:8099/#/user/login"
    def __init__(self, driver:WebDriver=None):
        """
        :param driver:
        """

        if driver is None:
            chrome_options = Options()
            # # Google\ Chrome - -remote - debugging - port = 9222
            # # 开启调试端口
            chrome_options.debugger_address = "127.0.0.1:9222"
            self._driver = webdriver.Chrome(options=chrome_options)
            # # self.driver = webdriver.Chrome()
            # self.driver.get("http://172.16.201.60:8099/#/user/login")
        else:
            self._driver = driver
        # self.driver=webdriver.Chrome()
        if self._base_url != None:
            self._driver.get(self._base_url)

    def find(self, by,locator):
        """定位元素"""
        return self._driver.find_element(by,locator)

    def wait_for_click(self, locator):
        """显示等待判断元素是否点击"""
        WebDriverWait(self._driver,10).until(expected_conditions.element_to_be_clickable(locator))

    def wait_for_click1(self, condition):
        WebDriverWait(self._driver,10).until(condition)





