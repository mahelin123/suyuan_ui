from selenium.webdriver.common.by import By

from common.basePage import BasePage
from pages.homePage import HomePage


class LoginPage(BasePage):
    def login(self, user, password):
        """
        登录,进入首页看板
        :param user:
        :param password:
        :return:
        """


        self.find(By.ID,"userName").send_keys(user)
        self.find(By.ID,"password").send_keys(password)
        self.find(By.XPATH,'//*[@id="formLogin"]/div[4]/div/div/span/button').click()
        # self._driver.find_element_by_id("userName").send_keys(user)
        # self._driver.find_element_by_id("password").send_keys(password)
        # self._driver.find_element_by_xpath('//*[@id="formLogin"]/div[4]/div/div/span/button').click()

        # return HomePage(self._driver)


# def logout(driver):
#     mouse = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[3]/div/span/span[2]')
#     ActionChains(driver).move_to_element(mouse).perform()
#     time.sleep(2)
#     driver.find_element_by_link_text("退出登录").click()
#     time.sleep(2)
#     driver.find_element_by_css_selector(".ant-btn-primary").click()
#     time.sleep(2)
#     driver.quit()
# if __name__ == "__main__":
#     driver = webdriver.Chrome()
#     driver.get("http://172.16.201.60:8099/#/user/login")
#     basepage = BasePage(driver)
#     LoginPage(driver).login("yueye", "Datac@123456")
#     time.sleep(2)
#     t = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[3]/div/span/span[2]').text
#     print("登录用户的名字%s" % t)
#     if t == "月野":
#         print("登录成功")
#     else:
#         print("登录失败")
