import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
print("test case Started")
driver.maximize_window()
driver.get("https://amazon.com")
time.sleep(1)

driver.find_element_by_id("twotabsearchtextbox").send_keys("samsung s20")
time.sleep(2)
driver.find_element_by_id("nav-search-submit-button").click()
time.sleep(6)


driver.close()
print("Test case has successfully completed")
