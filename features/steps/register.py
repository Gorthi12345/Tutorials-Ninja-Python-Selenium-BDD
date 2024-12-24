import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

from features.pages.AccountPage import AccountPage
from features.pages.HomePage import HomePage
from features.pages.registerPage import registerPage


@given(u'I navigated to the register page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.click_on_account_option()
    # context.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    # context.driver.find_element(By.LINK_TEXT,"Register").click()
    context.register_page = context.home_page.click_on_register_button()


@when(u'I entered the details into the all mandatory fields')
def step_impl(context):
    for row in context.table:
        context.register_page.enter_the_firstname_into_the_field(row["first_name"])
        context.register_page.enter_the_lastname_into_the_field(row["last_name"])
        context.register_page.enter_the_email_into_the_field(row["email"])
        context.register_page.enter_the_telephone_into_the_field(row["telephone"])
        context.register_page.enter_the_password_into_the_field(row["password"])
        context.register_page.enter_the_confirm_password_into_the_field(row["confirm_password"])
        context.register_page.click_the_agree_into_the_field()


@when(u'Click on the continue')
def step_impl(context):
    context.accountPage = context.register_page.click_on_continue()
    time.sleep(10)


@then(u'Account Should get Created')
def step_impl(context):
    context.accountPage.account_should_get_created("Your Account Has Been Created!")


@when(u'I entered the details into the all fields')
def step_impl(context):
    context.register_page.enter_the_firstname_into_the_field("John")
    context.register_page.enter_the_lastname_into_the_field("Targariyan")
    context.register_page.enter_the_email_into_the_field("raib@gmail.com")
    context.register_page.enter_the_telephone_into_the_field("1238979455")
    context.register_page.enter_the_password_into_the_field("123455689")
    context.register_page.enter_the_confirm_password_into_the_field("123455689")
    context.register_page.click_on_subscribe_choice()
    context.register_page.click_the_agree_into_the_field()


@when(u'I entered the details except email address')
def step_impl(context):
    context.register_page.enter_the_firstname_into_the_field("John")
    context.register_page.enter_the_lastname_into_the_field("Targariyan")
    context.register_page.enter_the_telephone_into_the_field("1238979455")
    context.register_page.enter_the_password_into_the_field("123455689")
    context.register_page.enter_the_confirm_password_into_the_field("123455689")
    context.register_page.click_the_agree_into_the_field()


@when(u'I entered the existing email address')
def step_impl(context):
    context.register_page.enter_the_email_into_the_field("kinglaying@gmail.com")


@then(u'Proper warning Message Should be about duplicate email address')
def step_impl(context):
    assert context.register_page.verifing_warning_message_for_duplicate_email_address(
        "Warning: E-Mail Address is already registered!")


@when(u'I do not enter the details into the  fields')
def step_impl(context):
    context.register_page.enter_the_firstname_into_the_field("")
    context.register_page.enter_the_lastname_into_the_field("")
    context.register_page.enter_the_email_into_the_field("")
    context.register_page.enter_the_telephone_into_the_field("")
    context.register_page.enter_the_password_into_the_field("")
    context.register_page.enter_the_confirm_password_into_the_field("")
    context.register_page.click_on_subscribe_choice()
    context.register_page.click_the_agree_into_the_field()


@then(u'Proper warning Message Should be displayed for every mandatory field')
def step_impl(context):
    policy_warning = "Warning: You must agree to the Privacy Policy!"
    firstname_warning = "First Name must be between 1 and 32 characters!"
    lastname_warning = "Last Name must be between 1 and 32 characters!"
    email_warning = "E-Mail Address does not appear to be valid!"
    mobile_warning = "Telephone must be between 3 and 32 characters!"
    password_warning = "Password must be between 4 and 20 characters!"
    # assert context.register_page.policy_alert_warning(policy_warning)
    assert context.register_page.first_name_warning(firstname_warning)


    assert context.register_page.last_name_warning(lastname_warning)
    assert context.register_page.email_warning(email_warning)
    assert context.register_page.telephone_warning(mobile_warning)
    assert context.register_page.password_warning(password_warning)
