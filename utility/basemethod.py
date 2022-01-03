import logging

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utility.pyrobot import Robot,Keys
from datetime import datetime

logging.basicConfig(filename = 'basemethod',level=logging.INFO)


class Services:

    """
        This method is to wait for presence of given element for given time(default timeout = 20 secs.)
        If element does not present in given max time, this will throw timeout exception.

        param locator: XPATH of given element
        param timeout: maximum wait timeout
    """
    def wait_for_element(self, driver, element, timeout=20):
        try:
            logging.info("# Wait for element to appear... ")
            WebDriverWait(driver, timeout).until(EC.presence_of_element_located((element[0], element[1])))
        except NoSuchElementException:
            logging.info("# Element  is not present.")

    """
        This method is to assert and click on the web driver.find_element(element[0], element[1]).

        param locator: XPATH of given element
        param_type: string
        """
    def assert_and_click(self, driver, element):
        try:
            logging.info("# Click on element")
            driver.find_element(element[0], element[1]).click()
        except NoSuchElementException:
            logging.info("# Element  is not present.")
            
    """
        This method is to enter value to the web driver.find_element(element[0], element[1]).

        param element: XPATH of given element
        param value
        """        
    def sendKeys(self, driver, element, value):
        try:
            driver.find_element(element[0], element[1]).send_keys(value)
        except NoSuchElementException:
            logging.info("# Element  is not present.")
            
    """
        This method is get the text present within given web driver.find_element(element[0], element[1]).

        param locator: XPATH of given element
        param_type: string
        """
    def get_text(self, driver, element):
        try:    
            return driver.find_element(element[0], element[1]).text
        except NoSuchElementException:
            logging.info("# Element  is not present.")
            
    """
        This method is to verify element is present or not.

        param locator: XPATH of given element
        param_type: string
        """
    def is_element_present(self, driver, element):
        try:
            driver.find_element(element[0], element[1]).is_element_present()
            logging.info("# Element  is present.")
            return True
        except NoSuchElementException:
            logging.info("# Element  is not present.")
            return False
        
    """
        This method is to assert element is present or not.

        param locator: XPATH of given element
        param_type: string
        """
    def assert_element_is_not_present(self, driver, element):
        
        logging.info("# Verifying Element is not present.")
        assert not driver.find_element(element[0], element[1]).is_element_present(), "Element  should not be present."
        
    """
        This method is to wait for visibility of given element for given time(default timeout = 20 secs.)
        If element does not present in given max time, this will throw timeout exception.

        param locator: XPATH of given element
        param_type: string

        param timeout: maximum wait timeout
        param_type: number
        """
    def wait_for_element_visible(self, driver, element, timeout=20):
        
        try:
            logging.info("# Wait for element to appear...")
            WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((element[0], element[1])))
        except NoSuchElementException:
            logging.info("# Element  is not present.")
    
    """
        This method is to wait for invisibility of given element for given time(default timeout = 20 secs.)
        If element does not present in given max time, this will throw timeout exception.

        param locator: XPATH of given element
        param_type: string

        param timeout: maximum wait timeout
        param_type: number
        """
    def wait_for_element_invisible(self, driver, element, timeout=20):
        
        try:
            logging.info("# Wait for element to appear... " )
            WebDriverWait(driver, timeout).until(EC.invisibility_of_element_located((element[0], element[1])))
        except NoSuchElementException:
            logging.info("# Element  is not present.")

    def is_element_visible(self, driver, element):
        try:
            return driver.find_element(element[0], element[1]).is_displayed()
        except NoSuchElementException:
            logging.info("# Element  is not present.")
        return False
    
    """
        This method is to assert element is present or not.

        param locator: XPATH of given element
        param_type: string
        """

    def assert_element_visibility(self, driver, element, is_visible=True):
       
        logging.info("# Verifying Element visibility.")
        assert is_visible == driver.find_element(element[0], element[1]).is_element_visible(), "Element  visibility should be %s." % (
            element, is_visible)
        
    def user_select_by_value(self, driver, element, value):
        try:
            logging.info("select_by_value %s", element)
            user_dropdown = Select(driver.find_element(element[0], element[1]))
            user_dropdown.select_by_value(value)
        except NoSuchElementException:
            logging.info("Unable to select ")
    
    def user_select_by_index(self, driver, element, value):

        try:
            logging.info("select_by_value %s", element)
            user_dropdown = Select(driver.find_element(element[0], element[1]))
            user_dropdown.select_by_index(value)
        except NoSuchElementException:
            logging.info("Unable to select ")

    def user_select_by_visible_text(self, driver, element, value):

        try:
            logging.info("select_by_value %s", element)
            user_dropdown = Select(driver.find_element(element[0], element[1]))
            user_dropdown.select_by_visible_text(value)
        except NoSuchElementException:
            logging.info("Unable to select ")
        
    def check_dropdown_value_selected(self, driver, element, index, exp_val):
        try:
            # index starts at 1
            user_dropdown = Select(driver.find_element(element[0], element[1]))
            user_dropdown.select_by_index(index)
            g1 = user_dropdown.first_selected_option
            act_val = g1.text
            if exp_val == act_val:
                ret = 0
                logging.info(f"values matched: index: {index}, exp_val: {exp_val},  act_val : {act_val}")
            else:
                ret = 1
                logging.info(f"Error: values did not match : index: {index}, exp_val: {exp_val},  act_val : {act_val}")
            return ret
        except NoSuchElementException:
            logging.info("Unable to get selected value ")
            return False
    
    def robot_capslock_on(self):
        robot = Robot()
        robot.key_press(Keys.caps_lock)
    
    def robot_capslock_off(self):
        robot = Robot()
        robot.key_release(Keys.caps_lock)
        
    def alert_accept(self, driver):
        try:
            logging.info("Handling the alert")
            a = driver.switch_to.alert
            a.accept()
        except NoAlertPresentException:
            logging.info("Alert not found")
            
        
    def alert_dismiss(self, driver):
        try:
            logging.info("Handling the alert")
            a = driver.switch_to.alert
            a.dismiss()
        except NoAlertPresentException:
            logging.info("Alert not found")
        
    def alert_sendkeys(self, driver):
        try:
            logging.info("Handling the alert")
            a = driver.switch_to.alert
            a.send_keys()
        except NoAlertPresentException:
            logging.info("Alert not found")
    
    def check_alert(self, driver, exp_err):
    
        msg = ""
        try:
            actual_error = driver.self.switch_to.alert.text()
            driver.switch_to.alert.accept()
    
            if exp_err != actual_error:
                logging.info("1. Error: Expected Msg (" + exp_err + ")  does not match Actual Msg (" + actual_error + ")")
                ret = 1
            else:
                logging.info("Expected Msg (" + exp_err + ")  matches Actual Msg (" + actual_error + ")")
                ret = 0
            return ret, msg
        except Exception as err:
            logging.info(err)
            return 1, msg
    
    def get_screenshot(self, driver, filename):
        d_time = datetime.now().strftime("%m_%d_%Y__%H_%M_%S")
        driver.get_screenshot_as_file(filename + d_time + ".png")
        
    
