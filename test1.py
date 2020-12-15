from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(executable_path="C:\seleniumdrivers\chromedriver.exe")
#driver = webdriver.Firefox(executable_path="C:\seleniumdrivers\geckodriver.exe")
#driver = webdriver.Ie(executable_path="C:\seleniumdrivers\IEDriverServer.exe")
driver.get("https://www.wordstream.com/")
print(driver.title)
assert "WordStream: Online Advertising Made Easy" in driver.title
print(driver.current_url)
driver.find_element_by_xpath("//*[@id='block-header-top-primary-menu']/ul/li[2]/a").click()
time.sleep(5)
driver.close()