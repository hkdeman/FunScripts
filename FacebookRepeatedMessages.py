from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time, random, requests, string, json

driver = webdriver.Firefox()
driver.get("https://www.facebook.com")
inputElement = driver.find_element_by_xpath('')
inputElement.send_keys(sentence)
driver.find_element_by_xpath('/html/body/div[6]/form/div[2]/input[1]').click()
   


