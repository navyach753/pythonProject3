from selenium import webdriver
import time
driver=webdriver.Chrome(executable_path="C:\seleniumdrivers\chromedriver.exe")
driver.get("http://testautomationpractice.blogspot.com/")

driver.find_element_by_xpath("//*[@id="HTML9"]/h2").click()
time.sleep(5)
# to move cursor to alert window use switch to alert
#driver.switch_to.alert().accept()  #closes alert windown by clciking ok
driver.switch_to.alert().dismiss()
driver.close()

