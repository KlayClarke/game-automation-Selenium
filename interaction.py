from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = '/Users/klayclarke/Desktop/Development/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(url='https://en.wikipedia.org/wiki/Main_Page')

article_count = driver.find_element(By.CSS_SELECTOR, '#articlecount a')

# article_count.click()

driver.find_element(By.LINK_TEXT, article_count.text).click()

# driver.quit()
