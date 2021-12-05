import sched, time
import selenium.webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException, ElementNotInteractableException

s = sched.scheduler(time.time, time.sleep)

chrome_driver_path = '/Users/klayclarke/Desktop/Development/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_driver_path)
action = webdriver.ActionChains(driver)

driver.get(url='http://orteil.dashnet.org/experiments/cookie/')

cookie = driver.find_element(By.ID, 'cookie')

upgrade_ids = ['buyCursor', 'buyGrandma', 'buyFactory', 'buyMine', 'buyShipment',
               'buyAlchemy lab', 'buyPortal', 'buyTime machine', 'buyElder Pledge']

available_upgrades = []
unavailable_upgrades = []


def check_upgrades():
    for id in upgrade_ids:
        element = driver.find_element(By.ID, id)
        element_class = element.get_attribute('class')
        if element_class == 'grayed':
            unavailable_upgrades.append(element)
        else:
            available_upgrades.append(element)

print(available_upgrades)
print(unavailable_upgrades)

# driver.quit()

#TODO: every 5 seconds, check right upgrade pane for available upgrades
#TODO: purchase the most expensive available upgrade
#TODO: compare the upgrade to your cookie count to gauge availability
