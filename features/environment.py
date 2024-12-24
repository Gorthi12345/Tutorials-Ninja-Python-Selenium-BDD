import allure
import openpyxl
from allure_commons.types import AttachmentType
from selenium import webdriver


from behave.model import ScenarioOutline

from utilities import configReader
from utilities.load_excel_data import load_data_from_excel


def before_feature(context, feature):
    print("Always Be Happy")
    if feature.name == "Login Functionality with Excel Data":
        file_path = "Book1.xlsx"  # Path to the Excel file
        data = load_data_from_excel(file_path)

        # Find all scenario outlines
        for scenario in feature.scenarios:
            if scenario.keyword == "Scenario Outline":
                examples_table = scenario.examples[0].table
                # Add rows from Excel to Examples table
                for row in data:
                    examples_table.add_row([row["email"], row["password"]])
def before_scenario(context,driver):
    browser = configReader.read_configurations("basic-info", "browser")
    if browser == "chrome":
        context.driver = webdriver.Chrome()
    elif browser == "edge":
        context.driver = webdriver.Firefox()
    else:
        context.driver = webdriver.Edge()

    context.driver.maximize_window()
    context.driver.get(configReader.read_configurations("basic-info", "url"))




def after_scenario(context,driver):
    context.driver.quit()

def after_step(context,step):
    if step.status == "failed":
        allure.attach(context.driver.get_screenshot_as_png(),
                      name="failed screenshot",
                      attachment_type=AttachmentType.PNG)