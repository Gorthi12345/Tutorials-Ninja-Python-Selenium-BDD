
from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self,driver):
        self.driver = driver

    def click_on_element(self,locator_type,locator_value):
        element = self.get_element(locator_type,locator_value)
        element.click()


    def verify_page_title(self,expectedd_title):
        return self.driver.title.__eq__(expectedd_title)

    def verify_text(self,locator_type,locator_value,verifying_text):
        element = self.get_element(locator_type, locator_value)
        return element.text.__eq__(verifying_text)

    def display_status(self,locator_type,locator_value):
        element = self.get_element(locator_type, locator_value)
        return element.is_displayed()

    def retrive_element_text_should_contain(self,locator_type,locator_value,expected_text):
        element = self.get_element(locator_type, locator_value)
        return element.text.__contains__(expected_text)

    def type_into_element(self,locator_type,locator_value,text_to_entered):
        element = self.get_element(locator_type,locator_value)
        element.click()
        element.clear()
        element.send_keys(text_to_entered)


    def get_element(self,locator_type,locator_value):
        element = None
        if locator_type.endswith("_id"):
            element = self.driver.find_element(By.ID,locator_value)
        elif locator_type.endswith("_name"):
            element = self.driver.find_element(By.NAME,locator_value)
        elif locator_type.endswith("_xpath"):
            element = self.driver.find_element(By.XPATH,locator_value)
        elif locator_type.endswith("_class_name"):
            element = self.driver.find_element(By.CLASS_NAME,locator_value)
        elif locator_type.endswith("_link_text"):
            element = self.driver.find_element(By.LINK_TEXT,locator_value)
        elif locator_type.endswith("_css"):
            element = self.driver.find_element(By.CSS_SELECTOR,locator_value)
        return element