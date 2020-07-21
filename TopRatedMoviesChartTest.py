from time import sleep

from ChartPageTestCase import IMDBChartHelper, IMDBNavigationLocators


def test_sort_by_imdb_rating_test_desc_asc(browser):
    imdb_chart_page = IMDBChartHelper(browser)
    imdb_chart_page.open_top_rated_movies_chart()
    imdb_chart_page.check_page_scroll()
    assert imdb_chart_page.check_numbers_of_content_top_rated_movies_chart() == 250
    imdb_chart_page.change_sort_type(IMDBNavigationLocators.IMDB_RATING_BTN)
    imdb_chart_page.find_element(IMDBNavigationLocators.IMDB_RATING_SELECTED)
    currentURL = browser.current_url
    assert 'sort=ir,desc' in currentURL
    imdb_chart_page.change_asc_desc_sort_type(IMDBNavigationLocators.CHOOSE_SORT_ASC)
    sleep(3)
    currentURL = browser.current_url
    assert 'sort=ir,asc' in currentURL


def test_add_to_watch_list_noauth(browser):
    imdb_share_url = IMDBChartHelper(browser)
    imdb_share_url.open_top_rated_movies_chart()
    imdb_share_url.add_element_to_watch_list_noauth()
    currentURL = browser.current_url
    assert '/registration/signin' in currentURL
