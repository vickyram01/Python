
import pytest
import logging
import data.Testdata as testdata

from Pages.LoginPage import  LoginPage as Login
from utility.drivermanager import DriverManager
import unittest

class Test_Login(unittest.TestCase):
    
    
            
    def test_01__valid_login_bmc(self):
        driver = DriverManager().setUp()
        username = testdata.username
        password  = testdata.password
        print(password)
        logging.info("Login with valid credentials")
        Login().loginWithCredentials(driver ,username, password)