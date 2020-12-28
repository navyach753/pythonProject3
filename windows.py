from selenium import webdriver
import selenium
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path="C:\seleniumdrivers\chromedriver.exe")
driver.get("http://demo.automationtesting.in/Windows.html")
driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()
print(driver.current_window_handle)#returns the parent window
handles=driver.window_handles #window_handles returns open window
print(handles)
for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title) #.title returns the title of the page
driver.quit()