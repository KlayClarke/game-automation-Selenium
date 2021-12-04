from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = '/Users/klayclarke/Desktop/Development/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(url='https://www.python.org/')

event_name_elements = driver.find_elements(By.CSS_SELECTOR, '.event-widget li a')
event_names = [event.text for event in event_name_elements]
event_date_elements = driver.find_elements(By.CSS_SELECTOR, '.event-widget li time')
event_dates = [date.text for date in event_date_elements]

event_info = {}
for i in range(len(event_names)):
    event_info[i] = {
        'time': event_dates[i],
        'name': event_names[i]
    }

print(event_info)

driver.quit()
