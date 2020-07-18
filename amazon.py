import time
import xlsxwriter 
from selenium import *
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.action_chains import ActionChains

chromedriver = "D:\\truelancer selenium python\\chromedriver_win32\\chromedriver.exe"
driver=webdriver.Chrome(executable_path=chromedriver)

keyword = 'hdpe grow bags'
total = 40

workbook = xlsxwriter.Workbook('new.xlsx') 
worksheet = workbook.add_worksheet()

keyword = keyword.replace(" ", "+")
siteId = 'https://www.amazon.in/s?k=' + keyword + '&ref=nb_sb_noss_2'

driver.get(siteId)
time.sleep(1)

row = 0
col = 0

for i in range (total):
	try:
		num = str(i+2)
		prod_Name = '//*[@id="search"]/div[1]/div[2]/div/span[3]/div[2]/div[' + num + ']/div/span/div/div/div[2]/h2/a/span'
		prod_Rating = '//*[@id="search"]/div[1]/div[2]/div/span[3]/div[2]/div[' + num + ']/div/span/div/div/div[3]/div/span[2]/a/span'
		prod_Price = '//*[@id="search"]/div[1]/div[2]/div/span[3]/div[2]/div[' + num + ']/div/span/div/div/div[4]/div[1]/div/a/span[1]/span[2]/span[2]'
		Name = driver.find_element_by_xpath(prod_Name).text
		Rating = driver.find_element_by_xpath(prod_Rating).text
		Price = driver.find_element_by_xpath(prod_Price).text
		worksheet.write(row, col, Name)
		worksheet.write(row, col+1, Rating)
		worksheet.write(row, col+2, Price)
		print(str(i) + " " + Name + " " + Rating + " " + Price)
		row+=1
	except:
		print(i)
		time.sleep(2)
		i = i-2
		pass

workbook.close()