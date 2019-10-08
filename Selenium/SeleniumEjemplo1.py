from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import io


option = webdriver.ChromeOptions()
option.add_argument(" — incognito")

browser = webdriver.Firefox(executable_path='D:\github.com\oswaldom-code\Python\Selenium\webDrive\geckodriver')

browser.get("https://www.vivaair.com/co/es/vuelo?DepartureCity=BOG&ArrivalCity=LIM&DepartureDate=2019-08-07&ReturnDate=2019-08-28&Adults=1&Currency=COP")

# Wait 20 seconds for page to load
timeout = 0
try:
    #WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//img[@class='avatar width-full rounded-2']")))
   
 # find_elements_by_xpath returns an array of selenium objects.
    #titles_element = browser.find_elements_by_xpath("//a[@class='text-bold']")
    # use list comprehension to get the actual repo titles and not the selenium objects.
    #titles = [x.text for x in titles_element]
    # print out all the titles.
    #print('titles:')
    #print(titles, '\n')
    
    soup = BeautifulSoup (browser.page_source, 'html.parser') 
    x = soup.find_all ('div', attrs = {'class': 'flights'})

    print(x)

   

    browser.quit()

except TimeoutException:
    print("Timed out waiting for page to load")
    

    """# find_elements_by_xpath returns an array of selenium objects.
    titles_element = browser.find_elements_by_xpath("//a[@class='text-bold']")
    # use list comprehension to get the actual repo titles and not the selenium objects.
    titles = [x.text for x in titles_element]
    # print out all the titles.
    print('titles:')
    print(titles, '\n')
    
    soup = BeautifulSoup (browser.page_source, 'html.parser') 
    x = soup.find_all ('div', attrs = {'class': 'flights'})

    print(x)
    browser.quit()"""

print("fin del codigo!")
browser.quit()