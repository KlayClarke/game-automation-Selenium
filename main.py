from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = '/Users/klayclarke/Desktop/Development/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(url='https://www.python.org/')
all_dates = driver.find_elements(By.CSS_SELECTOR, 'li time')
event_dates = all_dates[-5:]
event_dates_text = [date.text for date in event_dates]
print(event_dates_text)
driver.quit()
