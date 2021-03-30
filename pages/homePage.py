
import time
# from telnetlib import EC
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from common.basePage import BasePage


class HomePage(BasePage):
    """
    首页
    """
    def goto_RanchInformationPage(self):
        time.sleep(2)
        # element1=self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(3) > p:nth-child(1) img")\
        element1=(By.CSS_SELECTOR, "div:nth-child(3) > p:nth-child(1) img")
        # WebDriverWait(self.driver,timeout=2,poll_frequency=0.5).until(EC.presence_of_element_located(element1))
        WebDriverWait(self.driver,timeout=2,poll_frequency=0.5).until(EC.presence_of_element_located(element1))

        self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(3) > p:nth-child(1) img").click()

        # time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, "首页看板").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(3) > p:nth-child(2) img").click()
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, "首页看板").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(4) > p:nth-child(1) img").click()
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, "首页看板").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(4) > p:nth-child(2) img").click()
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, "首页看板").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(5) > p:nth-child(1) img").click()
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, "首页看板").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(5) > p:nth-child(2) img").click()
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, "首页看板").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(6) > p:nth-child(1) img").click()
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, "首页看板").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(6) > p:nth-child(2) img").click()
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, "首页看板").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "p:nth-child(3) img").click()
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, "首页看板").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(7) > p:nth-child(1) img").click()
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, "首页看板").click()
        time.sleep(2)
        element = self.driver.find_element(By.LINK_TEXT, "首页看板")
        time.sleep(2)
        # actions = ActionChains(self.driver)
        # actions.move_to_element(element).perform()
        # element = self.driver.find_element(By.CSS_SELECTOR, "body")
        # actions = ActionChains(self.driver)
        # actions.move_to_element(element, 0, 0).perform()
        # self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(7) > p:nth-child(2) img").click()
        # self.driver.find_element(By.LINK_TEXT, "首页看板").click()

    def goto_WarninginformationPage(self):
        self.driver.find_element(By.LINK_TEXT, "预警信息")
        return WarninginformationPage(self.driver)



