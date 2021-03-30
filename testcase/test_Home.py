from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from common.basePage import BasePage
from pages.homePage import HomePage
from pages.loginPage import LoginPage


class TestHome:



    def setup(self):
        chrome_options=Options()
        chrome_options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=chrome_options)
        # self.driver = webdriver.Chrome()
        self.driver.get("http://172.16.201.60:8099/#/user/login")
        self.login = LoginPage(self.driver)
        # self.login.login("yueye", "Datac@123456")

        self.home = HomePage(self.driver)
        self.home.goto_RanchInformationPage()
        # self.driver.get("http://172.16.201.60:8099/#/user/login")
        # self.login = LoginPage(self.driver)


    def test_3(self):
        print("test3")
        # self.home.goto_RanchInformationPage()

        assert 1 == 1

    def teardown(self):
        self.driver.quit()
