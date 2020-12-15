from selenium import webdriver
import selenium
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path="C:\seleniumdrivers\chromedriver.exe")
driver.get("https://www.wordstream.com/")
driver.find_element_by_xpath("//*[@id='block-header-top-primary-menu']/ul/li[2]/a").click()
ele=driver.find_element_by_xpath("//*[@id='login-email']")
print(ele.is_displayed())
print(ele.is_enabled())
ele.send_keys("hnkreddy@gmail.com")
time.sleep(5)
hnk=driver.find_element_by_xpath("//*[@id='login-password']")
print(hnk.is_displayed())
print(hnk.is_enabled())
hnk.send_keys("111111")
signwd=driver.find_element_by_xpath("/html/body/div[1]/div[6]/div/div/form/div[3]/div").click()
time.sleep(5)
driver.close()