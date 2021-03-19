from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\seleniumdrivers\chromedriver.exe")
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window() #command to maximize a window
#1. scroll down the page by pixel
#driver.execute_script("window.scrollBy(0,1000)","")
# 2. scroll downby find element
flagindia=driver.find_element_by_xpath("//*[@id='content']/div[2]/div[2]/table[1]/tbody/tr[86]/td[1]/img")
driver.execute_script("arguments[0].scrollIntoView();",flagindia)