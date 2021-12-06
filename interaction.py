import sched, time
from threading import Timer
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

upgrades = {}
upgrade_prices = {}

# try to put all upgrade attributes in one big dict
list_of_upgrades = driver.find_elements(By.CSS_SELECTOR, '#store div')
for upgrade in list_of_upgrades:
    # get all upgrade ids
    upgrade_id = upgrade.get_attribute('id')
    # get all upgrade prices
    try:
        upgrade_price = int(upgrade.text.split('\n')[0].split('-')[1])
    except ValueError:
        upgrade_price = upgrade.text.split('\n')[0].split('-')[1].replace(',', '')
    except IndexError:
        upgrade_price = 0
    print(upgrade_price)
    # place upgrade ids and prices in dict
    upgrade_dict_entry = {
        upgrade_id: {
            'price': upgrade_price,
            'element': upgrade
        }
    }
    upgrades.update(upgrade_dict_entry)


print(upgrades)

# driver.quit()

# TODO: get upgrade item ids
# TODO: get all upgrade items b tags - isolate price
# TODO: create dict of store items and prices
# TODO: get current cookie count
# TODO: isolate items that we can afford
# TODO: purchase most expensive upgrade we can afford
# TODO: rerun this every five seconds for five minutes
