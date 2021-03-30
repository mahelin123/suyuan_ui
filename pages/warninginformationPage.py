from selenium.webdriver.common.by import By

from common.basePage import BasePage


class WarninginformationPage(BasePage):
    """
    预警看板
    """
    def inquire(self):
        """
        查询
        :return:
        """
        self.driver.find_element(By.CSS_SELECTOR, ".ant-btn-primary:nth-child(1)").click()


    def reset(self):
        """
        重置
        :return:
        """
        self.driver.find_element(By.CSS_SELECTOR, ".ant-btn:nth-child(3)").click()


if __name__ == '__main__':
    WarninginformationPage(BasePage).inquire()

