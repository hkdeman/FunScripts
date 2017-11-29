from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

username = ""
password = ""
directory = ""
link = ""
driver = webdriver.Chrome(directory)
driver.get(link)
emailElement = driver.find_element_by_id('email')
emailElement.send_keys(username)
passElement = driver.find_element_by_id('pass')
passElement.send_keys(password)

driver.find_element_by_xpath('//*[@id="loginbutton"]').click()


actions = ActionChains(driver)

for i in range(200):
    actions.send_keys("Isn't that super cool?\n")
    actions.perform()
   


