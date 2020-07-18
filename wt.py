import time
import xlrd
from selenium import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

chromedriver = "D:\\truelancer selenium python\\chromedriver_win32\\chromedriver.exe"
driver=webdriver.Chrome(executable_path=chromedriver)

search = "Yash jss ise"

siteId = "https://web.whatsapp.com/"
btnPath = '//*[@id="side"]/div[1]/div/button'
driver.get(siteId)

for i in range (15):
	# driver.implicitly_wait(1)
	time.sleep(1)
	print(i)
driver.find_element_by_xpath(btnPath).click()
ActionChains(driver).send_keys(search).perform()
time.sleep(3)
ActionChains(driver).send_keys(Keys.RETURN).perform()
time.sleep(2)
for i in range(10):
	test = "Selenium test no " + str(i+1)
	ActionChains(driver).send_keys(test, Keys.RETURN).perform()

