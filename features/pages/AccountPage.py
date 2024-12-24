from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from features.pages.BasePage import BasePage


class AccountPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    edit_yout_account_for_knowing_link_text = "Edit your account information"
    verification_of_account_creation_xpath = "//div[@id='content']/h1"

    def edit_yout_account_asserti(self):

        try:
            # Attempt to find the element
            return self.display_status("edit_yout_account_for_knowing_link_text",
                                       self.edit_yout_account_for_knowing_link_text)


        except NoSuchElementException:
            # If the element is not found, return False
            return False

    def account_should_get_created(self,Creation_message):
        try:
            # Attempt to find the element
            return self.retrive_element_text_should_contain("verification_of_account_creation_xpath",self.verification_of_account_creation_xpath,Creation_message)


        except NoSuchElementException:
            # If the element is not found, return False
            return False
