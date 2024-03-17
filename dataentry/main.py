import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


FORM_URL = 'https://forms.gle/bj5y53NN5vJi7j9e7'
ZILLOW_URL = 'https://appbrewery.github.io/Zillow-Clone/'


response= requests.get(ZILLOW_URL)
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page,"html.parser")

#-----get a list of addresses -----
addresses = [address.getText().strip() for address in soup.find_all(name="address")]
print(addresses)
#-----get a list of links ----------
links = [link.get('href') for link in soup.find_all(class_ = "property-card-link")]
print(links)


#--------get a list of prices ------
prices = [price.text[0:6] for price in soup.find_all(class_ = "PropertyCardWrapper__StyledPriceLine")]
print(prices)




#-----FILL IN FORM -----------------
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options = chrome_options)

driver.get(FORM_URL)
time.sleep(5)

for n in range(0,len(addresses)):
    first_ques = driver.find_element(by=By.XPATH,
                                     value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    sec_ques = driver.find_element(by=By.XPATH,
                                   value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    third_ques = driver.find_element(by=By.XPATH,
                                     value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    send_button = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')

    first_ques.send_keys(addresses[n])
    sec_ques.send_keys(links[n])
    third_ques.send_keys(prices[n])
    send_button.click()
    resend_button = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    resend_button.click()

