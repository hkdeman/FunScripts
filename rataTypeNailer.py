from selenium import webdriver

driver = webdriver.FireFox()
driver.get("https://www.ratatype.com/typing-test/test/")
driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[1]/button').click()

