from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = '/Users/klayclarke/Desktop/Development/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(url='https://en.wikipedia.org/wiki/Main_Page')

search = driver.find_element(By.NAME, 'search')
search.send_keys('Python')
search.send_keys(Keys.ENTER)
# driver.quit()
