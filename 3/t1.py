from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

chrome_driver_path = "C:\\Users\\dell\\devops\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"
service = Service(executable_path=chrome_driver_path)

driver = webdriver.Chrome(service=service)
driver.get("https://www.google.com")
assert "Google" in driver.title
time.sleep(5)
driver.quit()
