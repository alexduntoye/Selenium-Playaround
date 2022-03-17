from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

PATH = '/Users/alexduntoye/chromedriver'

driver = webdriver.Chrome(PATH)

driver.get('https://www.pistonheads.com/')


time.sleep(10)

cookie_find = driver.find_element_by_xpath('//div[@id="qcCmpButtons"]')

button_find = cookie_find.find_element_by_xpath('//button[@class="qc-cmp-button"]').click()

time.sleep(5)

postcode_find = driver.find_element_by_xpath('//label[@for="car-finder-postcode"]')

postcode = postcode_find.find_element_by_xpath('//input[@data-type-id="car-finder-postcode"]')

postcode.send_keys("WD25 9UL")

time.sleep(5)

Make_find = driver.find_element_by_xpath('//label[@for="car-finder-make"]')
Make = Select(Make_find.find_element_by_xpath('//select[@id="car-finder-make"]'))
Make.select_by_value("2207")

time.sleep(5)

Model_find = driver.find_element_by_xpath('//label[@for="car-finder-model"]')
Model = Select(Model_find.find_element_by_xpath('//select[@id="car-finder-model"]'))
Model.select_by_value("2212")

time.sleep(5)

Search = driver.find_element_by_xpath('//button[@data-type-id="car-finder-search-button"]').submit()

time.sleep(7)

Result = driver.find_element_by_xpath('//a[@rel="IntCategoryv3:Classifieds.ResultsPage.Listings|Action:click|Label:headline.pos-3"]').click()

time.sleep(7)

Img = driver.find_element_by_xpath('//img[@src="//img.pistonheads.com/LargeSize/abarth/695/695-70th-1-4-tjet-180hp/abarth-695-695-70th-1-4-tjet-180hp-466277075-34.jpg"]').click()

time.sleep(5)

Next_1 = driver.find_element_by_xpath('//button[@title="Next (arrow right)"]').click()

time.sleep(4)

Next_2 = driver.find_element_by_xpath('//button[@title="Next (arrow right)"]').click()

time.sleep(4)


Next_3 = driver.find_element_by_xpath('//button[@title="Next (arrow right)"]').click()

time.sleep(4)

close = driver.find_element_by_xpath('//button[@title="Close (Esc)"]').click()

time.sleep(3)

homepage = driver.find_element_by_xpath('//img[@src="/static/images/logo-smiley-with-text.svg"]').click()

time.sleep(3)

driver.quit()

print("Goodnight! ;)")



#href="/classifieds/used-cars/abarth/695/abarth-695-695-70th-1-4-tjet-180hp/10529899"




#What i've learnt: if you're finding a particular element its always good to break it up branch by branch and drill down on it by variables



#<button class="qc-cmp-button" onclick="window.__cmpui(&quot;setAndSaveAllConsent&quot;,!0)"> Yes, that's ok </button>


'''''''''''''''
car_link = driver.find_element_by_link_text("Cars")
car_link.click()
time.sleep(3)


makes_link = Select(driver.find_element_by_id("brand"))
makes_link.select_by_value("pagani")
time.sleep(3)

submit = driver.find_element_by_xpath("//div[@class='submit form-group']/button").submit()
time.sleep(10)

result = driver.find_element_by_xpath("//*[@title='Pagani Huayra BC']")

result_action = ActionChains(driver)

result_action.click(on_element=result)

result_action.perform()

time.sleep(2)

driver.quit()
'''''''''''''''