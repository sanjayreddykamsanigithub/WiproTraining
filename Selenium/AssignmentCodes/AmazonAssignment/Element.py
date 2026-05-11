from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

# Open Amazon
driver.get("https://www.amazon.in")

# Search Smart Watches
search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.send_keys("Smart Watches")

search_button = driver.find_element(By.ID, "nav-search-submit-button")
search_button.click()

wait = WebDriverWait(driver, 20)

# Wait for results
wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "div.s-main-slot"))
)

# Scroll to brand section
driver.execute_script("window.scrollBy(0,1500);")
time.sleep(3)

# Click boAt brand checkbox
boat_brand = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'boAt')]"))
)

driver.execute_script("arguments[0].scrollIntoView();", boat_brand)
time.sleep(2)

driver.execute_script("arguments[0].click();", boat_brand)

# Wait for filtered results
time.sleep(5)

# Count products
products = driver.find_elements(
    By.CSS_SELECTOR,
    "div.s-main-slot div[data-component-type='s-search-result']"
)

print("Number of boAt Smart Watches on first page:", len(products))

time.sleep(10)  # Screenshot time

driver.quit()