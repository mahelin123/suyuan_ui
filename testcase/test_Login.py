import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from pages.loginPage import LoginPage


class Test_Login():
    # def setUp(self):
    def setup(self):
        # chrome_options = Options()
        # # Google\ Chrome - -remote - debugging - port = 9222
        # # 开启调试端口
        # chrome_options.debugger_address = "127.0.0.1:9222"
        # self.driver = webdriver.Chrome(options=chrome_options)
        # self.driver = webdriver.Chrome()
        # self._driver.get("http://172.16.201.60:8099/#/user/login")
        self.login = LoginPage()


    def test_1(self):
        self.login.login("yueye", "Datac@123456")
        time.sleep(2)

        # 断言
        # # t=self._driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[3]/div/span/span[2]').text
        # t=self.find(By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div[3]/div/span/span[2]').text()
        # # t=self._driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[3]/div/span/span[2]').text
        # #
        # print("登录用户的名字%s"%t)
        # if t=="月野":
        #     print("登录成功")
        # else:
        #     print("登录失败")

    def test_2(self):
        self.login.login("yueye", "Datac@12345")
        time.sleep(2)
        #断言
        t=self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[3]/div/span/span[2]').text
        print("登录用户的名字%s"%t)
        if t=="月野":
            print("登录成功")
        else:
            print("登录失败")

    # def teardown(self):
    #     self.driver1.quit()


