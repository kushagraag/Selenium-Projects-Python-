import time
import xlrd
from selenium import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

workbook = xlrd.open_workbook('info.xlsx')
worksheet = workbook.sheet_by_index(0)

chromedriver = str(worksheet.cell(26,1).value)
driver=webdriver.Chrome(executable_path=chromedriver)

def main():
	naukari()

def naukari():
	NaukariId = worksheet.cell(1,3).value
	NuakariPwd = str(int(worksheet.cell(2,3).value))
	JobName = worksheet.cell(5,3).value
	location = worksheet.cell(10,3).value
	workExpNo = int(worksheet.cell(8,3).value)
	salary = int(worksheet.cell(6,3).value)			# for .5 years enter 0 otherwise exact amount
	industry = worksheet.cell(12,3).value
	jobCategory = worksheet.cell(11,3).value 		#Department
	role = worksheet.cell(14,3).value
	name = worksheet.cell(13,3).value
	# all site id and locations
	site_id = "https://www.naukri.com/nlogin/login"
	createAlert_id = "https://www.naukri.com/free-job-alerts"
	password = """//*[@id="passwordField"]"""
	username = """//*[@id="usernameField"]"""
	signInBtn = """//*[@id="loginForm"]/div[3]/div[3]/div/button[1]"""
	JobPath = """//*[@id="Sug_kwdsugg"]"""
	locationPath = """//*[@id="Sug_locsugg"]"""
	workExp = """//*[@id="cjaExp"]"""
	salaryPath = """//*[@id="cjaMinSal"]"""
	industryPath = """//*[@id="cjaInd"]"""
	jobCategoryPath = """//*[@id="cjaJob"]"""
	rolePath = """//*[@id="cjaRole"]"""
	namePath = """//*[@id="nyja"]"""
	jobALertBtn = """//*[@id="cjaSubmit"]"""
	workStart = -1
	salaryStart = -1
	driver.get(site_id)
	driver.implicitly_wait(3)
	time.sleep(3)
	ele = driver.find_element_by_xpath(username).send_keys(NaukariId)
	driver.find_element_by_xpath(password).send_keys(NuakariPwd, Keys.RETURN)
	driver.implicitly_wait(4)
	time.sleep(4)
	driver.get(createAlert_id)
	driver.implicitly_wait(3)
	time.sleep(3)
	for i in range(20):
		try:
			driver.find_element_by_xpath(JobPath).send_keys(JobName)
			break
		except:
			driver.refresh()
			time.sleep(1)
			driver.implicitly_wait(1)
			pass
	driver.find_element_by_xpath(locationPath).send_keys(location, Keys.TAB)
	for x in range(workStart, workExpNo):
		driver.find_element_by_xpath(workExp).send_keys(Keys.DOWN)
	else:
		driver.find_element_by_xpath(workExp).send_keys(Keys.TAB)
	if(salary > 50):
		salary = salary - 50
		salary = salary / 5
		salary = int(salary)
		salary = salary+50
	for i in range(salaryStart, salary):
		driver.find_element_by_xpath(salaryPath).send_keys(Keys.DOWN)
	else:
		driver.find_element_by_xpath(salaryPath).send_keys(Keys.TAB)
	driver.find_element_by_xpath(industryPath).send_keys(industry, Keys.RETURN)
	driver.find_element_by_xpath(jobCategoryPath).send_keys(jobCategory, Keys.RETURN)
	driver.find_element_by_xpath(rolePath).send_keys(role, Keys.DOWN, Keys.RETURN)
	driver.find_element_by_xpath(namePath).send_keys(name, Keys.TAB, Keys.RETURN)
	print("Posted on times jobs")
	driver.implicitly_wait(4)
	time.sleep(4)
	
main()