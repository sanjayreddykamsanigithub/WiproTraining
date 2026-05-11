import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Launch browser
driver = webdriver.Chrome()
driver.maximize_window()

# Open Amazon
driver.get("https://www.amazon.in")

# Wait until search bar is visible
wait = WebDriverWait(driver, 15)
search_box = wait.until(
    EC.visibility_of_element_located((By.ID, "twotabsearchtextbox"))
)

# Enter product
search_box.send_keys("Wireless Headphones")

# Search button click
search_button = wait.until(
    EC.element_to_be_clickable((By.ID, "nav-search-submit-button"))
)
search_button.click()

# Wait for results
wait.until(
    EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Wireless Headphones')]"))
)

print("Search results for Wireless Headphones displayed successfully")
time.sleep(10)
driver.quit()