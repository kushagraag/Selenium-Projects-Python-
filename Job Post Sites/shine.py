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
	shineJobs()

def shineJobs():
	# enter emailid and pass for shine
	ShineId = worksheet.cell(1,2).value
	ShinePwd = worksheet.cell(2,2).value
	# REFER TO READMEE FILE FOR INSTRUCTIONS ON HOW TO ENTER VALUES FOR SALARY AND EXPERIENCE
	jobName = worksheet.cell(5,2).value
	salary = str(int(worksheet.cell(6,2).value))
	experience = str(int(worksheet.cell(8,2).value))
	location = worksheet.cell(10,1).value
	department = worksheet.cell(11,2).value
	industry = worksheet.cell(12,2).value
	name = worksheet.cell(13,2).value
	site_id = "https://www.shine.com/myshine/login/"
	username = """//*[@id="id_email"]"""
	password = """//*[@id="id_password"]"""
	postJobSite_id = "https://www.shine.com/myshine/free-job-alerts/"
	jobNamePath = """//*[@id="id_keywords"]"""
	salaryPath = """/html/body/div[2]/div/div[2]/div[2]/form/ul[1]/li[2]/span/select"""
	experiencePath = """/html/body/div[2]/div/div[2]/div[2]/form/ul[1]/li[3]/span/select"""
	locationPath = """/html/body/div[2]/div/div[2]/div[2]/form/ul[1]/li[4]/span/div/button"""
	inputLocationPath = """/html/body/div[2]/div/div[2]/div[2]/form/ul[1]/li[4]/span/div/div/div/input"""
	departmentPath = """/html/body/div[2]/div/div[2]/div[2]/form/ul[1]/li[5]/div/div/button"""
	inputDepartmentPath = """/html/body/div[2]/div/div[2]/div[2]/form/ul[1]/li[5]/div/div/div/div/input"""
	industryPath = """/html/body/div[2]/div/div[2]/div[2]/form/ul[1]/li[6]/div/div/button"""
	inputIndustryPath = """/html/body/div[2]/div/div[2]/div[2]/form/ul[1]/li[6]/div/div/div/div/input"""
	nameofAlertPath = """/html/body/div[2]/div/div[2]/div[2]/form/ul[1]/li[9]/input"""
	createBtnPath = """/html/body/div[2]/div/div[2]/div[2]/form/ul[2]/li/div/a"""
	driver.get(site_id)
	ele = driver.find_element_by_xpath(username).send_keys(ShineId)
	driver.find_element_by_xpath(password).send_keys(ShinePwd, Keys.RETURN)
	driver.implicitly_wait(1)
	driver.get(postJobSite_id)
	driver.find_element_by_xpath(jobNamePath).send_keys(jobName)
	Select(driver.find_element_by_xpath(salaryPath)).select_by_value(salary)
	Select(driver.find_element_by_xpath(experiencePath)).select_by_value(experience)
	driver.find_element_by_xpath(locationPath).click()
	driver.find_element_by_xpath(inputLocationPath).send_keys(location, Keys.TAB, Keys.SPACE)
	driver.find_element_by_xpath(departmentPath).click()
	driver.find_element_by_xpath(inputDepartmentPath).send_keys(department, Keys.TAB, Keys.SPACE)
	driver.find_element_by_xpath(industryPath).click()
	driver.find_element_by_xpath(inputIndustryPath).send_keys(industry, Keys.TAB, Keys.SPACE)
	driver.find_element_by_xpath(nameofAlertPath).send_keys(name)
	driver.find_element_by_xpath(createBtnPath).click()
	print("Posted on shine jobs")
	driver.implicitly_wait(4)

main()