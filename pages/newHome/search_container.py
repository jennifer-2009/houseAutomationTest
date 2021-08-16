from pages.newHome.locators import SetSearchHouseLocators
from pages.base_page import BasePage
from utils.selenium_utils import SeleniumUtils


class SearchContainer(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def set_user_input(self, searchKey):
        self.wait_element(*SetSearchHouseLocators.search_box).send_keys(searchKey)
        self.driver.find_element(*SetSearchHouseLocators.search_button).click()



    def get_filter_box(self):
        utils = SeleniumUtils(self.driver)
        return utils.get_text(*SetSearchHouseLocators.filter_box_city)
