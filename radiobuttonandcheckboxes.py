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
radiobutton_mrs=driver.find_element_by_id("uniform-id_gender2")
radiobutton_mrs.click()
driver.find_element_by_id("customer_firstname").send_keys("vennela")
driver.find_element_by_id("customer_lastname").send_keys("oneu")
driver.find_element_by_id("email").clear()
driver.find_element_by_id("email").send_keys("redy.navya@gmail.com")
driver.find_element_by_id("passwd").send_keys("5525252")
time.sleep(5)
driver.close()