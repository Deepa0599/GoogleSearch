import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
print("test case Started")
driver.maximize_window()
driver.get("https://instagram.com/")
time.sleep(5)
driver.find_element_by_name("username").send_keys("")
time.sleep(5)
driver.find_element_by_name("password").send_keys("")
time.sleep(10)
driver.find_element_by_name("login").click()



driver.close()
print("Test case has successfully completed")