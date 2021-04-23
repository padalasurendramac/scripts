from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from time import sleep


username = "test" 

password = "test"


url = "https://www.facebook.com"


driver = webdriver.Chrome()


driver.get(url)


driver.find_element_by_id("email").send_keys(username)

driver.find_element_by_id("pass").send_keys(password)


#s = driver.find_elements_by_Class_name('_42ft _4jy0 _6lth _4jy6 _4jy1 selected _51sy')

#(By.CLASS_NAME, "content")

#s = driver.find_elements_by_name("login")
s = driver.find_element_by_xpath("//button[@name='login']")

s.click()
