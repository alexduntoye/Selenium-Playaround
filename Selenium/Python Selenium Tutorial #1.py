from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time

PATH = '/Users/alexduntoye/chromedriver'
driver = webdriver.Chrome(PATH)

driver.get('https://www.autotrader.co.uk/')

postcode = driver.find_element_by_name("postcode")
postcode.send_keys("WD25 9UL")
postcode.send_keys(Keys.RETURN)

time.sleep(3)

select_make = Select(driver.find_element_by_name("make"))

select_make.select_by_index(9)

time.sleep(1)

select_model = Select(driver.find_element_by_name("model"))

select_model.select_by_index(17)

time.sleep(1)


link = driver.find_element_by_link_text("Prestige cars")
link.click()

'''try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Bugatti"))
    )
    element.click()
except:
    driver.quit()
'''

time.sleep(4)

driver.back()




print(driver.page_source)

time.sleep(7)

driver.quit()