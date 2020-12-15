from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\seleniumdrivers\chromedriver.exe")
driver.get("https://www.wordstream.com/")
print(driver.title)
print(driver.current_url)
driver.get("https://www.buzzfeed.com")
print(driver.title)
print(driver.current_url)
driver.back()
print(driver.title)
driver.forward()
print(driver.title)
time.sleep(5)
driver.close()