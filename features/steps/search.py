from behave import  *
from selenium import webdriver
from selenium.webdriver.common.by import By

from features.pages.HomePage import HomePage
from features.pages.searchPage import searchPage


@given(u'I got navigated to Home Screen')
def step_impl(context):
    context.homepage = HomePage(context.driver)
    assert context.homepage.verify_hometitie("Your Store")



@when(u'I entered the valid input to the Search Box')
def step_impl(context):
    context.homepage.enter_prodyct_into_searchbox("HP")


@when(u'Click on the Search Button')
def step_impl(context):
    context.search_page = context.homepage.click_on_search_button()


@then(u'Valid Product Should get displayed in the results')
def step_impl(context):
    assert  context.search_page.valid_product_display_in_results()

@when(u'I entered the InValid input to the Search Box')
def step_impl(context):
    context.homepage.enter_prodyct_into_searchbox("Honda")

@then(u'Proper message should be get displayed in the results')
def step_impl(context):
    expected_text = "There is no product that matches the search criteria."
    assert context.search_page.propermessage_should_be_displayed_in_the_results_for_invalid(expected_text)

@when(u'I do not enter the input in the search box')
def step_impl(context):
    context.homepage.enter_prodyct_into_searchbox("")