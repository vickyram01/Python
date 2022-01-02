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
    def wait_for_element(self, element, timeout=20):
        try:
            logging.info("# Wait for element to appear... %s" % element)
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(element))
        except NoSuchElementException:
            logging.info("# Element '%s' is not present." % element)

    """
        This method is to assert and click on the web element.

        param locator: XPATH of given element
        param_type: string
        """
    def assert_and_click(self, element):
        try:
            self.wait_for_element(element)
            logging.info("# Click on element %s" % element)
            element.click()
        except NoSuchElementException:
            logging.info("# Element '%s' is not present." % element)
            
    """
        This method is to enter value to the web element.

        param element: XPATH of given element
        param value
        """        
    def sendKeys(self, driver, element, value):
        try:
            driver.find_element(element).send_keys(value)
        except NoSuchElementException:
            logging.info("# Element '%s' is not present." % element)
            
    """
        This method is get the text present within given web element.

        param locator: XPATH of given element
        param_type: string
        """
    def get_text(self, element):
        try:    
            return element.text
        except NoSuchElementException:
            logging.info("# Element '%s' is not present." % element)
            
    """
        This method is to verify element is present or not.

        param locator: XPATH of given element
        param_type: string
        """
    def is_element_present(self, element):
        try:
            element.is_element_present()
            logging.info("# Element '%s' is present." % element)
            return True
        except NoSuchElementException:
            logging.info("# Element '%s' is not present." % element)
            return False
        
    """
        This method is to assert element is present or not.

        param locator: XPATH of given element
        param_type: string
        """
    def assert_element_is_not_present(self, locator):
        
        logging.info("# Verifying Element is not present.")
        assert not self.is_element_present(locator), "Element '%s' should not be present." % locator
        
    """
        This method is to wait for visibility of given element for given time(default timeout = 20 secs.)
        If element does not present in given max time, this will throw timeout exception.

        param locator: XPATH of given element
        param_type: string

        param timeout: maximum wait timeout
        param_type: number
        """
    def wait_for_element_visible(self, element, timeout=20):
        
        try:
            logging.info("# Wait for element to appear... %s" % element)
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(element))
        except NoSuchElementException:
            logging.info("# Element '%s' is not present." % element)
    
    """
        This method is to wait for invisibility of given element for given time(default timeout = 20 secs.)
        If element does not present in given max time, this will throw timeout exception.

        param locator: XPATH of given element
        param_type: string

        param timeout: maximum wait timeout
        param_type: number
        """
    def wait_for_element_invisible(self, element, timeout=20):
        
        try:
            logging.info("# Wait for element to appear... %s" % element)
            WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(element))
        except NoSuchElementException:
            logging.info("# Element '%s' is not present." % element)

    def is_element_visible(self, element):
        try:
            return element.is_displayed()
        except NoSuchElementException:
            logging.info("# Element '%s' is not present." % element)
        return False
    
    """
        This method is to assert element is present or not.

        param locator: XPATH of given element
        param_type: string
        """

    def assert_element_visibility(self, element, is_visible=True):
       
        logging.info("# Verifying Element visibility.")
        assert is_visible == self.is_element_visible(element), "Element '%s' visibility should be %s." % (
            element, is_visible)
        
    def user_select_by_value(self, element, value):
        try:
            logging.info("select_by_value %s", element)
            user_dropdown = Select(self.find_element(*element))
            user_dropdown.select_by_value(value)
        except NoSuchElementException:
            logging.info("Unable to select '%s'" % element)
    
    def user_select_by_index(self, element, value):

        try:
            logging.info("select_by_value %s", element)
            user_dropdown = Select(self.find_element(*element))
            user_dropdown.select_by_index(value)
        except NoSuchElementException:
            logging.info("Unable to select '%s'" % element)

    def user_select_by_visible_text(self, element, value):

        try:
            logging.info("select_by_value %s", element)
            user_dropdown = Select(self.find_element(*element))
            user_dropdown.select_by_visible_text(value)
        except NoSuchElementException:
            logging.info("Unable to select '%s'" % element)
        
    def check_dropdown_value_selected(self, element, index, exp_val):
        try:
            # index starts at 1
            user_dropdown = Select(self.find_element(*element))
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
            logging.info("Unable to get selected value '%s'" % element)
            return False
    
    def robot_capslock_on(self):
        robot = Robot()
        robot.key_press(Keys.caps_lock)
    
    def robot_capslock_off(self):
        robot = Robot()
        robot.key_release(Keys.caps_lock)
        
    def alert_accept(self):
        try:
            logging.info("Handling the alert")
            a = self.switch_to.alert
            a.accept()
        except NoAlertPresentException:
            logging.info("Alert not found")
            
        
    def alert_dismiss(self):
        try:
            logging.info("Handling the alert")
            a = self.switch_to.alert
            a.dismiss()
        except NoAlertPresentException:
            logging.info("Alert not found")
        
    def alert_sendkeys(self):
        try:
            logging.info("Handling the alert")
            a = self.switch_to.alert
            a.send_keys()
        except NoAlertPresentException:
            logging.info("Alert not found")
    
    def check_alert(self, exp_err):
    
        msg = ""
        try:
            actual_error = self.switch_to.alert.text()
            self.switch_to.alert.accept()
    
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
    
    def get_screenshot(self, filename):
        d_time = datetime.now().strftime("%m_%d_%Y__%H_%M_%S")
        self.get_screenshot_as_file(filename + d_time + ".png")
        
    
