from datetime import datetime

from behave import *

from features.pages.AccountPage import AccountPage
from features.pages.HomePage import HomePage
from features.pages.LoginPage import LoginPage
from utilities import EmailGenerator


@given(u'I got navigated to login page')
def step_impl(context):
    context.homepage = HomePage(context.driver)
    context.homepage.click_on_account_option()
    context.loginpage = context.homepage.click_on_Login_option()


@when(u'I will enter the valid email address as "{email}" and valid password as "{password}" into the fields')
def step_impl(context, email, password):
    context.loginpage.enter_the_email(email)
    context.loginpage.enter_the_password(password)


@when(u'I click on the login button')
def step_impl(context):
    context.accountpage = context.loginpage.click_on_login()


@then(u'I should get logged in')
def step_impl(context):
    assert context.accountpage.edit_yout_account_asserti()


@when(u'I will enter the Invalid email address and valid password into the fields')
def step_impl(context):
    mailId = EmailGenerator.Getting_email()
    context.loginpage.enter_the_email(mailId)
    context.loginpage.enter_the_password("killingdevara")


@then(u'I should get a proper error message')
def step_impl(context):
    assert context.loginpage.status_of_warning_message("Warning: No match for E-Mail Address and/or Password.")


@when(u'I will enter the valid email address and Invalid password into the fields')
def step_impl(context):
    context.loginpage.enter_the_email("redsea@gmail.com")
    context.loginpage.enter_the_password("killingdeva")


@when(u'I will enter the Invalid email address and Invalid password into the fields')
def step_impl(context):
    mailId = EmailGenerator.Getting_email()
    context.loginpage.enter_the_email(mailId)
    context.loginpage.enter_the_password("killingdevara")


@when(u'I do not enter the email address and password into the fields')
def step_impl(context):
    context.loginpage.enter_the_email("")
    context.loginpage.enter_the_password("")

