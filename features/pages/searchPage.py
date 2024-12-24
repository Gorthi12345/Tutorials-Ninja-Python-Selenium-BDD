from selenium.webdriver.common.by import By

from features.pages.BasePage import BasePage


class searchPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)


    valid_product_link_text = 'HP LP3065'
    proper_message_for_invalid_data_xpath = "//div[@id='content']/p[2]"
    def valid_product_display_in_results(self):
        return self.display_status("valid_product_link_text",self.valid_product_link_text)


    def propermessage_should_be_displayed_in_the_results_for_invalid(self,expected_message):
        return self.verify_text("proper_message_for_invalid_data_xpath",
                                self.proper_message_for_invalid_data_xpath, expected_message)