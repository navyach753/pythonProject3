from selenium import webdriver
import selenium
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path="C:\seleniumdrivers\chromedriver.exe")
driver.get("http://automationpractice.com/")
driver.implicitly_wait(5)
driver.find_element_by_xpath("//*[@id='header']/div[2]/div/div/nav/div[1]/a").click()
email_ele=driver.find_element_by_name("email_create")
print(email_ele.is_displayed())
print(email_ele.is_enabled())
email_ele.send_keys("redy.navya@gmail.com")
driver.find_element_by_xpath("//*[@id='SubmitCreate']/span").click()

driver.close()