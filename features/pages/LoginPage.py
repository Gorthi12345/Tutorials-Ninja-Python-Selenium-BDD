from selenium.webdriver.common.by import By

from features.pages.AccountPage import AccountPage
from features.pages.BasePage import BasePage


class LoginPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)



    email_address_name = "email"
    password_name = "password"
    login_button_xpath = "//input[@value='Login']"
    warning_message_xpath = "//div[@class='alert alert-danger alert-dismissible']"





    def enter_the_email(self,email):
        self.type_into_element("email_address_name", self.email_address_name, email)

    def enter_the_password(self,password):
        self.type_into_element("password_name", self.password_name, password)


    def click_on_login(self):
        self.click_on_element("login_button_xpath", self.login_button_xpath)
        return AccountPage(self.driver)

    def status_of_warning_message(self,expected_waring):
        return self.retrive_element_text_should_contain("warning_message_xpath",self.warning_message_xpath,expected_waring)