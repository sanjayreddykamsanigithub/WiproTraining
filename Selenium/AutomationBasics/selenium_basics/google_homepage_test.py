from time import sleep

from selenium import webdriver
from selenium.webdriver.ie.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

browser = input('what browser do you want to use?')
match (browser.lower()):
    case 'chrome':
        driver = webdriver.Chrome(service=Service('../resources/chromedriver.exe'))
    case 'edge':
        driver = webdriver.edge(service=Service('../resources/chromedriver.exe'))
    case _:
        print('Unknown browser - Not available.' \n Executing with default CHROME browser.')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver = webdriver.Edge(service=Service('../resources/msedgedriver.exe'))
driver.get("https://www.google.com")

pagetitle = driver.title

if pagetitle == 'Google':
    print("Google Homepage loaded - Pass")
else:
    print("Google Homepage NOT loaded - Fail")
sleep(3)
driver.quit()



