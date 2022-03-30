import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver=webdriver.Chrome(ChromeDriverManager().install())
print("Test case Started")
driver.maximize_window()
driver.get("https://www.facebook.com/")
time.sleep(5)
driver.find_element_by_name("email").send_keys("")
time.sleep(5)
driver.find_element_by_name("pass").send_keys("")
time.sleep(10)
driver.find_element_by_name("login").click()
driver.close()
print("Test case has successfully completed")