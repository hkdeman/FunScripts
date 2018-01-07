from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import os 
import urllib
import time

def login(driver):
	username = ""
	password = ""


	username_input = driver.find_element_by_name("username")
	password_input = driver.find_element_by_name("password")


	username_input.send_keys(username)
	password_input.send_keys(password)

	password_input.send_keys(Keys.RETURN)



dirpath = os.getcwd()

driver = webdriver.Chrome("./chromedriver")

driver.get("http://moodle2.gla.ac.uk/my/")

login(driver)

source_code = driver.page_source

subjects = []

soup = BeautifulSoup(source_code,"lxml")
for link in soup.find_all("div",{"class":"courses-view-course-item"}):
	driver.get(link.a["href"])
	soup = BeautifulSoup(driver.page_source,"lxml")
	subject_name = soup.find("div",{"class":"page-header-headings"}).text
	subjects.append({"name":subject_name,"link":link.a["href"]})
	if not os.path.exists(subject_name):
		os.makedirs(subject_name)


for subject in subjects: 
	new_dir = dirpath+"/"+subject["name"]
	driver.close()	

	chrome_options = webdriver.ChromeOptions()
	prefs = {'download.default_directory' : new_dir,"plugins.plugins_list": [{"enabled":False,"name":"Chrome PDF Viewer"}]}
	chrome_options.add_experimental_option('prefs', prefs)
	driver = webdriver.Chrome("./chromedriver",chrome_options=chrome_options)
	driver.get(subject["link"])
	login(driver)

	for elements in driver.find_elements_by_class_name("resource"):
		elements.find_element_by_tag_name("a").click()
		notDownloaded=True
		while(notDownloaded):
			for f in os.listdir(new_dir):
				if(f.endswith(".crdownload")):
					time.sleep(1)
					continue
				notDownloaded=False

#	for downloadable in driver.find_elements_by_tag_name("a"):
#		if("pdf" in downloadable.get_attribute("href")):
#			try:
#				driver.get(downloadable.get_attribute("href"))
#			except:
#				pass
	
	folders = driver.find_elements_by_class_name("folder")
	for folder in folders:
		new_directory = new_dir+"/"+folder.text
		if not os.path.exists(new_directory):
			os.makedirs(new_directory)
		sub_folder_link = folder.find_element_by_tag_name("a").get_attribute("href")
		chrome_options = webdriver.ChromeOptions()
		prefs = {'download.default_directory' : new_directory ,"plugins.plugins_list": [{"enabled":False,"name":"Chrome PDF Viewer"}]}
		chrome_options.add_experimental_option('prefs', prefs)
		new_driver = webdriver.Chrome("./chromedriver",chrome_options=chrome_options)
		new_driver.get(sub_folder_link)
		login(new_driver)
		new_driver.find_element_by_xpath("//*[contains(text(), 'Download folder')]").click()
		time.sleep(5)
		notDownloaded=True
		while(notDownloaded):
			for f in os.listdir(new_directory):
				if(f.endswith(".crdownload")):
					time.sleep(5)
					continue
				notDownloaded=False
		new_driver.close()
		


driver.close()


