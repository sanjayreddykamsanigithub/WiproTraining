import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

# Implicit Wait
driver.implicitly_wait(10)

driver.get("https://www.amazon.in")
driver.maximize_window()

# Search laptop
search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.send_keys("Dell Inspiron Laptop")
driver.find_element(By.XPATH, "//input[@value='Go']").click()

# Explicit Wait for first product image
wait = WebDriverWait(driver, 15)
first_product = wait.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "img.s-image"))
)

# Click first result
first_product.click()

print("First laptop product opened successfully")
time.sleep(5)
driver.quit()