from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as ec
import logging
from contextlib import contextmanager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import staleness_of


class IMDBBase:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "http://www.imdb.com/"
        self.logger = logging.getLogger(__name__)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(ec.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(ec.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_main_page(self):
        return self.driver.get(self.base_url)

    def click_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(ec.element_to_be_clickable(locator)).click()

    def check_scroll_down(self, element_down):
        actions = ActionChains(self.driver)
        element_down = self.find_element(locator=element_down, time=2)
        actions.move_to_element(element_down).perform()

    def check_scroll_up(self, element_up):
        actions = ActionChains(self.driver)
        element_up = self.find_element(locator=element_up, time=2)
        actions.move_to_element(element_up).perform()

    @contextmanager
    def wait_for_page_load(self, element, timeout=30):
        old_page = self.find_element(locator=element)
        yield
        WebDriverWait(self.driver, timeout).until(staleness_of(old_page))
