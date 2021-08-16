from selenium.webdriver.common.by import By


class SetSearchHouseLocators:
    search_box = (By.CSS_SELECTOR, ".filter-search-input input[type='search']")
    search_button = (By.CSS_SELECTOR, ".filter-search-input>div>button")
    #
    filter_box_city = (By.CSS_SELECTOR, ".filter-detail-box>span:nth-child(1)")

