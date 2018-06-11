# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, thread, sys, os

class TPRLoginSelenium2(unittest.TestCase):
	def setUp(self):
		firefox_profile = webdriver.FirefoxProfile()
		firefox_profile.set_preference("browser.privatebrowsing.autostart", True)
		USERNAME = "user001"
		self.driver = webdriver.Firefox(firefox_profile=firefox_profile)
		self.driver.implicitly_wait(30)
		self.base_url = "http://18.204.231.208:9080"
		self.verificationErrors = []
		self.accept_next_alert = True
		
	def test_t_p_r_login_selenium2(self):
		driver = self.driver
		print("Opening Login page")
		driver.get(self.base_url + "/tpr-ui/POC-2/#/")
		driver.find_element_by_id("mat-input-0").clear()
		driver.find_element_by_id("mat-input-1").clear()
		print("Logging in as user: "+self.USERNAME)
		driver.find_element_by_id("mat-input-0").send_keys(self.USERNAME)
		driver.find_element_by_id("mat-input-1").send_keys("Aurotech77")
		driver.find_element_by_xpath("//button[@type='submit']").click()
		self.driver.implicitly_wait(10)
		print("Verify User as: "+self.USERNAME)
		for i in range(60):
			try:
				if "TprUi" == driver.title: break
			except: pass
			time.sleep(1)
		else: self.fail("time out")
		user_title = driver.find_element_by_css_selector("h5.card-title").text;
		# if self.USERNAME.upper() in user_title:
		print("User verified. Title is: ", user_title)
		print("Logging out")
		try: self.assertTrue(self.is_element_present(By.ID, "logout"))
		except AssertionError as e: self.verificationErrors.append(str(e))
		driver.find_element_by_xpath("//div[@class='file-input-column']//button[.='Browse']").click()
		self.driver.implicitly_wait(10)
		file_name = self.USERNAME+".xlsx"; 
		os.system("C:\\Users\\Anudeep\\Desktop\\TPR_File_Upload.exe "+file_name);
		for i in range(60):
			try:
				if file_name == driver.find_element_by_xpath("//div[@id='content']/div[2]/div/div/div/form/div/div/div/table/tbody/tr/td").text: break
			except: pass
			time.sleep(1)
		else: self.fail("time out")
		driver.find_element_by_xpath("//button[@type='submit']").click()

		self.driver.implicitly_wait(10)
		for i in range(120):
			try:
				if "File is completely uploaded! We are processing your file now. ThankYou." == driver.find_element_by_css_selector("h5").text: break
			except: pass
			time.sleep(1)
		else: self.fail("time out")
	
		# driver.find_element_by_id("logout").click()

	def is_element_present(self, how, what):
		try: self.driver.find_element(by=how, value=what)
		except NoSuchElementException as e: return False
		return True

	def is_alert_present(self):
		try: self.driver.switch_to_alert()
		except NoAlertPresentException as e: return False
		return True

	def close_alert_and_get_its_text(self):
		try:
			alert = self.driver.switch_to_alert()
			alert_text = alert.text
			if self.accept_next_alert:
				alert.accept()
			else:
				alert.dismiss()
			return alert_text
		finally: self.accept_next_alert = True

	def tearDown(self):
		self.driver.quit()
		self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
	if len(sys.argv) > 1:
		TPRLoginSelenium2.USERNAME = sys.argv.pop()
	unittest.main()
