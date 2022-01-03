import logging
import unittest
import sys, os
from pathlib import Path


from selenium import webdriver
import utility.config as config

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)



class  DriverManager():
    """
    This class is for instantiating web driver instances.
    """

    def setUp(self):
        """
        This method is to instantiate the web driver instance.
        """
        logging.info("## SETUP METHOD ##")
        logging.info("# Initializing the webdriver.")
        ROOT_PATH = str(Path(__file__).parent.parent)
        browser_name = config.browser
        if browser_name == "chrome":
            self.driver = webdriver.Chrome(executable_path=ROOT_PATH + os.sep + "drivers" + os.sep + "chromedriver.exe")
        elif self.browser_name == "firefox":
            self.driver = webdriver.Firefox(executable_path=ROOT_PATH + "/drivers\\geckodriver.exe")
        elif self.browser_name == "ie":
            self.driver = webdriver.Ie(executable_path=ROOT_PATH + "/drivers\\IEDriverServer.exe")
    
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get(config.url)  # get the url from conf file
        return self.driver

    def tearDown(self):
        """
        This is teardown method.
        It is to capture the screenshots for failed test cases,
        & to remove web driver object.
        """
        logging.info("## TEARDOWN METHOD ##")

        if sys.exc_info()[0]:
            logging.info("# Taking screenshot.")
            test_method_name = self._testMethodName
            self.driver.save_screenshot("./../screenshots/%s.png" % test_method_name)

        if self.driver is not None:
            logging.info("# Removing the webdriver.")
            self.driver.quit()

    def create_ffprofile(self):
        """
        This function is to create firefox profile.
        :return: firefox profile.
        """
        logging.info("# Setting up firefox profile.")
        profile = webdriver.FirefoxProfile()
        profile.set_preference('browser.download.folderList', 2)  # custom location
        profile.set_preference('browser.download.manager.showWhenStarting', False)
        profile.set_preference('browser.download.dir', os.getcwd())
        profile.set_preference('browser.helperApps.neverAsk.saveToDisk',
                               'text/csv,application/octet-stream,application/pdf,application/vnd.ms-excel')
        profile.set_preference("pdfjs.disabled", True)

        return profile

