from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch Chrome browser
driver = webdriver.Chrome()

# Open Amazon homepage
driver.get("https://www.amazon.in")

# Maximize browser
driver.maximize_window()

# Capture title
title = driver.title
print("Page Title:", title)

# Verify title contains Amazon
assert "Amazon" in title, "Amazon title verification failed"

# Wait for page load
time.sleep(6)

# Navigate to Mobiles category
driver.find_element(By.LINK_TEXT, "Mobiles").click()

# Wait for mobiles page
time.sleep(5)

# Go back to homepage
driver.back()

# Wait for homepage
time.sleep(5)

# Close browser
driver.quit()