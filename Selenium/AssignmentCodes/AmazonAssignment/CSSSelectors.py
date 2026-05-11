from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.amazon.in")
driver.maximize_window()

# Scroll to footer
driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)

time.sleep(3)

# Click About Us using link text
about_us = driver.find_element(By.LINK_TEXT, "About Amazon")
about_us.click()

time.sleep(5)

# Find Careers link and print text
careers = driver.find_element(By.LINK_TEXT, "Careers")
print("Element Text:", careers.text)

time.sleep(10)  # Screenshot time

driver.quit()