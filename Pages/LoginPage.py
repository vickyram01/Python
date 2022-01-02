from selenium import webdriver
from selenium.webdriver.common.by import By
from utility.basemethod import Services as base
from selenium.common.exceptions import NoSuchElementException
import logging




class LoginPage:

	USERNAME_FIELD = (By.XPATH, "//input[@id='identity']")
	PASSWORD_FIELD = (By.XPATH,  "//input[@id='password']")
	LOGIN_BUTTON = (By.XPATH,  "//button[@id='loginbutton']")
	DASHBOARD_FIELD = (By.XPATH, "//*[@id='root']/div/div/main/section/section/div[1]/div[1]")
	WRONG_MESS = (By.XPATH, "//p[contains(text(),'The provided username and/or password are incorrect.')]")
	LOG_OUT = (By.XPATH, "/html/body/div[1]/div/div/header/div/div[2]/div[3]/button")
	
	def loginWithCredentials(self, driver, username, password):

		try:
			base().sendKeys(driver, *LoginPage.USERNAME_FIELD, username)
			base().sendKeys(driver, *LoginPage.PASSWORD_FIELD, password)
			base().assert_and_click(driver, *LoginPage.LOGIN_BUTTON)
			base().wait_for_element_visible(driver, *LoginPage.DASHBOARD_FIELD)
		except NoSuchElementException:
			logging.info("element not found")
		
	def clickOnSubmit(self):
		base.assert_and_click(self, *LoginPage.LOGIN_BUTTON)
		base.wait_for_element_visible(self, *LoginPage.DASHBOARD_FIELD)
		
	def enterUsername(self, username):
		base.sendKeys(self, *LoginPage.USERNAME_FIELD, username)
		base.wait_for_element_visible(self, *LoginPage.DASHBOARD_FIELD)
		
	def enterPassword(self, password):
		base.sendKeys(self, *LoginPage.USERNAME_FIELD, password)
		base.wait_for_element_visible(self, *LoginPage.DASHBOARD_FIELD)
		