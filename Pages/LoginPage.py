from selenium import webdriver
from selenium.webdriver.common.by import By
from utility.basemethod import Services as base
from selenium.common.exceptions import NoSuchElementException
import logging




class LoginPage:
	
	def __init__(self):

		self.USERNAME_FIELD = (By.XPATH, "//input[@id='identity']")
		self.PASSWORD_FIELD = (By.XPATH,  "//input[@id='password']")
		self.LOGIN_BUTTON = (By.XPATH,  "//button[@id='loginbutton']")
		self.DASHBOARD_FIELD = (By.XPATH, "//*[@id='root']/div/div/main/section/section/div[1]/div[1]")
		self.WRONG_MESS = (By.XPATH, "//p[contains(text(),'The provided username and/or password are incorrect.')]")
		self.LOG_OUT = (By.XPATH, "/html/body/div[1]/div/div/header/div/div[2]/div[3]/button")
	
	def loginWithCredentials(self, driver, username, password):

		try:
			base().sendKeys(driver, self.USERNAME_FIELD, username)
			base().sendKeys(driver, self.PASSWORD_FIELD, password)
			base().assert_and_click(driver, self.LOGIN_BUTTON)
		except NoSuchElementException:
			logging.info("element not found")
		
	def clickOnSubmit(self, driver):
		base().assert_and_click(driver, self.LoginPage.LOGIN_BUTTON)
		base().wait_for_element_visible(driver, self.LoginPage.DASHBOARD_FIELD)
		
	def enterUsername(self, driver, username):
		base().sendKeys(driver, self.LoginPage.USERNAME_FIELD, username)
		base().wait_for_element_visible(driver, self.LoginPage.DASHBOARD_FIELD)
		
	def enterPassword(self, driver, password):
		base().sendKeys(driver, self.LoginPage.USERNAME_FIELD, password)
		base().wait_for_element_visible(driver, self.LoginPage.DASHBOARD_FIELD)
		