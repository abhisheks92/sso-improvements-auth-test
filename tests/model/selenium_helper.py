from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from tests.config import BASE_URL, HEADLESS
from selenium.webdriver.chrome.options import Options


class SeleniumHelper(object):

    def __init__(self):
        self.driver = None
        self.__driver_path = None
        self.create_chrome()

    def create_chrome(self):
        """
        Creates a chrome instance to run the tests on chrome browser
        :return:
        """
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.__driver_path = ChromeDriverManager().install()
        if HEADLESS:
            self.driver = webdriver.Chrome(self.__driver_path, options=chrome_options)
        else:
            self.driver = webdriver.Chrome(self.__driver_path)
        self.driver.get(BASE_URL)
        self.driver.maximize_window()

    def find(self, web_element, visible=True):
        """
        wrapper for finding the element by xpath
        :param web_element:
        :param visible:
        :return:
        """
        element = self.driver.find_element(By.XPATH, web_element)
        if visible is True and not element.is_displayed():
            raise Exception({
                "message": "Element not visible."
            })
        return element

    def quit(self):
        """
        Quit the browser instance
        :return:
        """
        self.driver.quit()
