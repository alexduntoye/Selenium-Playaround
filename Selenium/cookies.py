import pickle
import pprint

import time

from selenium import webdriver


def save_cookies(driver, location):
    pickle.dump(driver.get_cookies(), open(location, "wb"))


def load_cookies(driver, location=None, url=None):
    cookies = pickle.load(open(location, "rb"))
    driver.delete_all_cookies()

    url = "https://www.pistonheads.com/" if url is None else url
    driver.get(url)
    for cookie in cookies:
        driver.add_cookie(cookie)



def delete_cookie(driver, domains=None):
    cookies = driver.get_cookies()
    for cookie in cookies:
        if domains is not None:
            if str(cookie["domain"]) in domains:
                cookies.remove(cookie)
        else:
            driver.delete_all_cookies()
            return

    driver.delete_all_cookies()
    for cookie in cookies:
        driver.add_cookie(cookie)


PATH = '/Users/alexduntoye/chromedriver'

driver = webdriver.Chrome(PATH)

driver.get('https://www.pistonheads.com/')

time.sleep(10)

cookie_find = driver.find_element_by_xpath('//div[@id="qcCmpButtons"]')

button_find = cookie_find.find_element_by_xpath('//button[@class="qc-cmp-button"]').click()

time.sleep(2)

pprint.pprint(driver.get_cookies())

print("==============================\n")

save_cookies(driver, location='cookies.txt')

driver.quit()

#load_cookies(driver, "/Users/alexduntoye/PycharmProjects/Web Crawler_Scraper_BS4_Selenium/Selenium/cookies.txt")

#driver.get('https://www.pistonheads.com/')

#time.sleep(10)

load_cookies(driver, "/Users/alexduntoye/PycharmProjects/Web Crawler_Scraper_BS4_Selenium/Selenium/cookies.txt")

pprint.pprint(driver.get_cookies())

print("==============================\n")

'''''''''
<div class="qc-cmp-ui-content"> <p class="qc-cmp-title"> Welcome to PistonHeads </p> <span> <p class="qc-cmp-main-messaging"> This site uses Cookies to provide you with the best possible experience. To learn more please view our <a href="https://www.pistonheads.com/privacy-policy/#cookie-notice" target="_blank">Cookie Notice</a>.<br><br>We and our partners process your personal data to serve personalised advertising, measure activity on the site and deliver personalised features and content to you.  You have choice in who uses your data and for what purposes. You can come back at anytime to amend your Advertising Preferences. Please confirm to the use of your data in this way. </p> </span> <div class="qc-cmp-buttons qc-cmp-primary-buttons" id="qcCmpButtons"><button class="qc-cmp-button qc-cmp-secondary-button">MORE OPTIONS</button> <button class="qc-cmp-button" onclick="window.__cmpui(&quot;setAndSaveAllConsent&quot;,!0)"> Yes, that's ok </button> </div> </div>

< span > < p


class ="qc-cmp-main-messaging" > This site uses Cookies to provide you with the best possible experience.To learn more please view our < a href="https://www.pistonheads.com/privacy-policy/#cookie-notice" target="_blank" > Cookie Notice < / a >.< br > < br > We and our partners process your personal data to serve personalised advertising, measure activity on the site and deliver personalised features and content to you.You have choice in who uses your data and for what purposes.You can come back at anytime to amend your Advertising Preferences.Please confirm to the use of your data in this way.< / p > < / span >

< div


class ="qc-cmp-buttons qc-cmp-primary-buttons" id="qcCmpButtons" > < button class ="qc-cmp-button qc-cmp-secondary-button" > MORE OPTIONS < / button > < button class ="qc-cmp-button" onclick="window.__cmpui(&quot;setAndSaveAllConsent&quot;,!0)" > Yes, that's ok </button> </div>
'''''''''

