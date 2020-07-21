import random
from time import sleep
from IMDBBase import IMDBBase
from selenium.webdriver.common.by import By


class IMDBNavigationLocators:
    MAIN_MENU_BTN = (By.CSS_SELECTOR, "[aria-label='Open Navigation Drawer'].ipc-button")
    TOP_RATED_MOVIES = (By.XPATH, "//a[@href='/chart/top/?ref_=nv_mv_250']")
    MENU_HIDDEN = (By.XPATH, "[role='presentation'][aria-hidden='false']")
    MOVIE_TITLE = (By.CSS_SELECTOR, ".titleColumn")
    SORT_BTN = (By.XPATH, "//select[@name='sort']")
    IMDB_RATING_BTN = (By.XPATH, "//select[@id='lister-sort-by-options']/option[contains(text(),'IMDb Rating')]")
    IMDB_RATING_SELECTED = (By.XPATH, "//select[@id='lister-sort-by-options']/option[contains(text(),"
                                      "'IMDb Rating')][ "
                                      "@selected='selected']")
    CHOOSE_SORT_ASC = (By.XPATH, "//*[@title='Descending order']")
    CHOOSE_SORT_DESC = (By.XPATH, "//*[@title='Ascending order']")
    ADD_TO_WATCH_LIST_BTNS = (By.XPATH, "//*[@title='Click to add to watchlist']")
    SIGN_IN_BLOCK_MOVIE_CARD = (By.XPATH, "//*[@id='signin-options']")
    SCROLL_UP_ELEMENT = (By.CSS_SELECTOR, "h1.header")
    SCROLL_DOWN_ELEMENT = (By.XPATH, "//*[@class='imdb-footer__links']")


class IMDBChartHelper(IMDBBase):

    def __init__(self, driver):
        super().__init__(driver)

    def click_on_the_menu_button(self):
        return self.click_element(IMDBNavigationLocators.MAIN_MENU_BTN, time=2)

    def click_on_the_top_rated_movies(self):
        return self.click_element(IMDBNavigationLocators.TOP_RATED_MOVIES, time=2)

    def open_top_rated_movies_chart(self):
        self.go_to_main_page()
        self.click_on_the_menu_button()
        self.click_on_the_top_rated_movies()
        self.wait_for_page_load(IMDBNavigationLocators.MENU_HIDDEN)

    def change_sort_type(self, sort_type):
        self.find_element(IMDBNavigationLocators.SORT_BTN, time=5).click()
        self.find_element(locator=sort_type, time=5).click()
        self.driver.refresh()
        sleep(2)

    def change_asc_desc_sort_type(self, type):
        self.find_element(locator=type, time=5).click()

    def add_element_to_watch_list_noauth(self):
        movies = self.find_elements(IMDBNavigationLocators.ADD_TO_WATCH_LIST_BTNS)
        random_movie = random.choice(movies)
        random_movie.click()
        sleep(3)
        self.find_element(IMDBNavigationLocators.SIGN_IN_BLOCK_MOVIE_CARD)

    def check_numbers_of_content_top_rated_movies_chart(self):
        movies = self.find_elements(IMDBNavigationLocators.MOVIE_TITLE)
        number = len(movies)
        return number

    def check_page_scroll(self):
        self.check_scroll_up(IMDBNavigationLocators.SCROLL_DOWN_ELEMENT)
        self.check_scroll_down(IMDBNavigationLocators.SCROLL_UP_ELEMENT)
