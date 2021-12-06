import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException

chrome_driver_path = '/Users/klayclarke/Desktop/Development/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_driver_path)
action = webdriver.ActionChains(driver)

driver.get(url='http://orteil.dashnet.org/experiments/cookie/')

cookie = driver.find_element(By.ID, 'cookie')

upgrades = {}

list_of_upgrades = driver.find_elements(By.CSS_SELECTOR, '#store div')
# try to put all upgrade attributes in one big dict
for upgrade in list_of_upgrades:
    # get all upgrade ids
    upgrade_id = upgrade.get_attribute('id')
    # get all upgrade prices
    try:
        upgrade_price = int(upgrade.text.split('\n')[0].split('-')[1])
    except ValueError:
        upgrade_price = int(upgrade.text.split('\n')[0].split('-')[1].replace(',', ''))
    except IndexError:
        upgrade_price = 1000000000
    # place upgrade ids and prices in dict
    upgrade_dict_entry = {
        upgrade_price: {
            'id': upgrade_id,
        }
    }
    upgrades.update(upgrade_dict_entry)

in_five_sec = time.time() + 5
in_five_min = time.time() + 300

run_game = True

# run game - click nonstop
while run_game:
    cookie.click()
    # this code should run every 5 seconds
    if time.time() > in_five_sec:
        upgrade_prices = []
        # get user cookie count
        try:
            cookie_count = int(driver.find_element(By.ID, 'money').text)
        except ValueError:
            cookie_count = int(driver.find_element(By.ID, 'money').text.replace(',', ''))
        # compare cookie count to upgrade prices
        for key in upgrades.keys():
            key_price = key
            if cookie_count > key_price:
                upgrade_prices.append(key_price)
        # click most expensive available upgrade
        most_expensive_available_upgrade = upgrade_prices[-1]
        most_expensive_id = upgrades[most_expensive_available_upgrade]['id']
        button = driver.find_element(By.ID, most_expensive_id)
        button.click()
        # reset timer
        in_five_sec = time.time() + 5
    # after five minutes, stop game
    if time.time() > in_five_min:
        print(f'Cookies per sec: {cookie_count}')
        run_game = False
        driver.quit()

# TODO: get upgrade item ids
# TODO: get all upgrade items b tags - isolate price
# TODO: create dict of store items and prices
# TODO: get current cookie count
# TODO: isolate items that we can afford
# TODO: purchase most expensive upgrade we can afford
# TODO: rerun this every five seconds for five minutes
