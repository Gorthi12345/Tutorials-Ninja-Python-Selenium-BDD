from selenium.webdriver.common.by import By

from features.pages.BasePage import BasePage
from features.pages.LoginPage import LoginPage
from features.pages.registerPage import registerPage
from features.pages.searchPage import searchPage


class HomePage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    Account_option_xpath = "//a[@class='dropdown-toggle']/span"
    login_option_link_text = "Login"
    searh_box_name = 'search'
    search_button_xpath = '//button[@class="btn btn-default btn-lg"]'
    register_option_link_text = "Register"
    def click_on_account_option(self):
        self.click_on_element("Account_option_xpath",self.Account_option_xpath)

    def click_on_Login_option(self):
        self.click_on_element("login_option_link_text", self.login_option_link_text)
        return LoginPage(self.driver)

    def verify_hometitie(self,expected_title):
        return self.verify_page_title(expected_title)


    def enter_prodyct_into_searchbox(self,prouct_name):
        self.type_into_element("searh_box_name", self.searh_box_name, prouct_name)

    def click_on_search_button(self):

        self.click_on_element("search_button_xpath", self.search_button_xpath)
        return searchPage(self.driver)

    def click_on_register_button(self):
        self.click_on_element("register_option_link_text", self.register_option_link_text)
        return registerPage(self.driver)