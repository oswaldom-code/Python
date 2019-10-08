import pandas as pd
from selenium import webdriver


driver = webdriver.Firefox(executable_path=r"C:/Users/Beba/Documents/GitHub/Python/drivers/geckodriver.exe")
driver.get('http://google.com')
print(driver.title)
driver.quit()


