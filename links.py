from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\seleniumdrivers\chromedriver.exe")
driver.get("https://www.wordstream.com")
links=driver.find_elements(By.TAG_NAME,"a")
print("number of links on this page are:", len(links))
for link in links:
    print(link.text)
#clicking on the link
driver.find_element_by_link_text("Blog").click()
driver.close()