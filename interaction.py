from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = '/Users/klayclarke/Desktop/Development/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(url='http://secure-retreat-92358.herokuapp.com/')

first_name = driver.find_element(By.NAME, 'fName')
first_name.send_keys('Klay')
last_name = driver.find_element(By.NAME, 'lName')
last_name.send_keys('Clarke')
email = driver.find_element(By.NAME, 'email')
email.send_keys('testing@test.test')

email.send_keys(Keys.ENTER)

# driver.quit()
