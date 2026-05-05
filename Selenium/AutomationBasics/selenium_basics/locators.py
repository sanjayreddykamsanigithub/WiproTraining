import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.core import driver

'''driver = webdriver.Edge(service=Service('../resources/msedgedriver.exe'))
driver.get("https://www.google.com")
'''
#id
'''search_input = driver.find_element(By.ID, "APjFqb")
search_input.send_keys("selenium")
time.sleep(3)'''

#Name
'''search_input = driver.find_element(By.NAME, "q")
search_input.send_keys("locators")
time.sleep(3)'''

#Name
'''googlesearch_button = driver.find_element(By.NAME, "btnK")
googlesearch_button.click()
time.sleep(30)'''

#Classname
'''infl_button = driver.find_element(By.CLASS_NAME, "RNmpXc")
infl_button.click()
time.sleep(3)'''

#TagName
'''href_element = driver.find_elements(By.TAG_NAME, 'a')
for elmt in href_element:
    print(f'{elmt.text} - {elmt.get_attribute('href')}')'''

#LinkText
'''images_link = driver.find_element(By.LINK_TEXT, "Images")
images_link.click()
time.sleep(10)'''

#Partial LinkText
'''images_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Ima")
images_link.click()
time.sleep(10)'''

#CSS Selectors
'''search_input = driver.find_element(By.CSS_SELECTOR, 'div > textarea')
search_input.send_keys("Selenium")
time.sleep(5)

settings_text = driver.find_element(By.XPATH, '/html/body/div[2]/div[7]/div/div[2]/div[2]2/span/span/g-popup/div[1]/div')
print(settings_text.text)
time.sleep(5)'''

driver.get("https://the-internet.herokuapp.com/tables")
time.sleep(5)

'''and_example = driver.find_element(By.XPATH, "//td[text()='Tim' and @class='first-name']")
print(f"AND Example -> Found with both conditions: {and_example.text}")'''

'''ancestor_table = driver.find_element(By.XPATH, "//td[text()='jsmith@gmail.com']/ancestor::table")
print(f"Ancestor Example "'''