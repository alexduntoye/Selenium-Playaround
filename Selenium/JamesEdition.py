from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.common.action_chains import ActionChains

PATH = '/Users/alexduntoye/chromedriver'

driver = webdriver.Chrome(PATH)

driver.get('https://www.jamesedition.com/')

time.sleep(7)

real_estate = driver.find_element_by_xpath('//a[@title="Real Estate"]').click()

time.sleep(7)

most_expensive_house = driver.find_element_by_xpath('//a[@href="/real_estate/beverly-hills-ca-usa/authentic-italian-village-10678761"]').click()

time.sleep(7)

#cookies_find = driver.find_element_by_xpath('//button[@class="cookie__button js-cookie__button"]').click()

#time.sleep(5)

most_expensive_house_slide_show = driver.find_element_by_xpath('//img[@src="https://img.jamesedition.com/listing_images/2019/10/07/11/07/04/32efb206-bfed-461d-9fc6-51a270de8b19/je/2000xxs.jpg"]').click()

time.sleep(10)

next_image = driver.find_element_by_xpath('//div[@class="je2-listing-gallery__current-image"]')
next_image.send_keys(Keys.ARROW_RIGHT)










