from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = '/Users/klayclarke/Desktop/Development/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(url='https://en.wikipedia.org/wiki/Main_Page')

num_of_articles = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
print(num_of_articles.text)

driver.quit()