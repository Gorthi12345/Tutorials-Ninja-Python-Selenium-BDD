from selenium.webdriver.common.by import By

from features.pages.AccountPage import AccountPage
from features.pages.BasePage import BasePage


class registerPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)


    first_name_id = "input-firstname"
    last_name_id = "input-lastname"
    email_field_id = "input-email"
    telephone_id = "input-telephone"
    password_id = "input-password"
    confirm_password_id = "input-confirm"
    agree_checkbox_name = "agree"
    click_continue_xpath = "//input[@value='Continue']"
    subscribe_selection_xpath = "//input[@name='newsletter'][@value='1']"
    warning_message_for_duplicate_email_xpath = "//div[@class='alert alert-danger alert-dismissible']"
    policy_warning_xpath = "//div[@class='alert alert-danger alert-dismissible']"
    firstname_warning_xpath = "//input[@id='input-firstname']/following-sibling::div"
    lastname_warning_xpath = "(//div[@class='col-sm-10']/div)[3]"
    email_warning_xpath = "(//div[@class='col-sm-10']/div)[4]"
    mobile_warning_xpath = "(//div[@class='col-sm-10']/div)[5]"
    password_warning_xpath = "(//div[@class='col-sm-10']/div)[6]"



    def enter_the_firstname_into_the_field(self,firstname):
        self.type_into_element("first_name_id", self.first_name_id, firstname)


    def enter_the_lastname_into_the_field(self,lastname):
        self.type_into_element("last_name_id", self.last_name_id, lastname)


    def enter_the_email_into_the_field(self,email):
        self.type_into_element("email_field_id", self.email_field_id, email)

    def enter_the_telephone_into_the_field(self,telepone):
        self.type_into_element("telephone_id", self.telephone_id, telepone)

    def enter_the_password_into_the_field(self,password):
        self.type_into_element("password_id", self.password_id, password)

    def enter_the_confirm_password_into_the_field(self,confirmPassword):
        self.type_into_element("confirm_password_id", self.confirm_password_id, confirmPassword)


    def click_the_agree_into_the_field(self):
        self.click_on_element("agree_checkbox_name", self.agree_checkbox_name)

    def click_on_continue(self):
        self.click_on_element("click_continue_xpath", self.click_continue_xpath)
        return AccountPage(self.driver)

    def click_on_subscribe_choice(self):
        self.click_on_element("subscribe_selection_xpath", self.subscribe_selection_xpath)


    def verifing_warning_message_for_duplicate_email_address(self,duplicateMail_Warning):
        return self.verify_text("warning_message_for_duplicate_email_xpath",self.warning_message_for_duplicate_email_xpath,duplicateMail_Warning)


    def policy_alert_warning(self,policy_warning):
        return self.verify_text("policy_warning_xpath",self.policy_warning_xpath, policy_warning)

    def first_name_warning(self,firstname_warning):
        return self.verify_text("firstname_warning_xpath",self.firstname_warning_xpath, firstname_warning)


    def last_name_warning(self,lastname_warning):
        return self.verify_text("lastname_warning_xpath",self.lastname_warning_xpath, lastname_warning)


    def email_warning(self,emailaddress_warning):
        return self.verify_text("email_warning_xpath",self.email_warning_xpath, emailaddress_warning)

    def telephone_warning(self,telephone_warning):
        return self.verify_text("mobile_warning_xpath",self.mobile_warning_xpath, telephone_warning)


    def password_warning(self,pass_warning):
        return self.verify_text("password_warning_xpath", self.password_warning_xpath, pass_warning)