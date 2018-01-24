from selenium import webdriver
import threading
from selenium.webdriver.common.keys import Keys

##xpath = input('Enter the xpath of the dropdown\n')

def crawl():    
    driver = webdriver.Firefox()
    url ='https://www.eventbrite.co.uk/e/do-you-have-the-guts-2017-tickets-38119507473#tickets'
##    url ='https://www.eventbrite.co.uk/e/2017-scottish-open-grand-prix-shuttle-time-big-hit-festivals-glasgow-schools-only-weekday-tickets-37644122584?aff=es2#tickets'
    driver.get(url)
    
    tag = driver.find_elements_by_tag_name('select')[0].get_attribute('id')

    driver.find_element_by_xpath('//*[@id="'+tag+'"]/option[2]').click()
    driver.find_element_by_xpath('//*[@id="event-page"]/div[11]/div[2]/div/div/section[3]/div/div/div[3]/button').click()
    
threads = []

for i in range(10):
    t = threading.Thread(target=crawl)
    threads.append(t)
    t.start()


