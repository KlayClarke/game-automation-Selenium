from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = '/Users/klayclarke/Desktop/Development/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(url='https://www.amazon.com/Neumann-87-Ai-Set-Microphone/dp/B00502CCXG/?_encoding=UTF8&pd_rd_w=MmRCm'
               '&pf_rd_p=29505bbf-38bd-47ef-8224-a5dd0cda2bae&pf_rd_r=A16QKW2WNNQ6CQA3HHZG&pd_rd_r=ff5578c4-4c44-43fc'
               '-87f9-c435b07d0d8c&pd_rd_wg=FrK1F&ref_=pd_gw_ci_mcx_mr_hp_atf_m')
product_title = driver.find_element(By.ID, 'productTitle')
print(product_title.text)

driver.quit()