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
	hirist()


def hirist():
	HiristId = worksheet.cell(1,4).value
	HiristPwd = worksheet.cell(2,4).value

	jobTitle = worksheet.cell(5,4).value
	location = worksheet.cell(10,4).value
	yearsOfExperienceMin = str(int(worksheet.cell(8,4).value))
	yearsOfExperienceMax = str(int(worksheet.cell(9,4).value))
	jobDescription = worksheet.cell(24,4).value
	category = 	worksheet.cell(11,4).value 						#Department
	functionalArea = worksheet.cell(12,4).value 					#industry
	
	site_id = "https://recruit.hirist.com/login"
	postJobSite_id = "https://recruit.hirist.com/post-job?ref=nav"
	username = """//*[@id="email"]"""
	password = """//*[@id="password"]"""
	signInBtn = """//*[@id="login"]"""
	jobTitlePath = """//*[@id="title"]"""
	locationPath = """//*[@id="location"]"""
	yearsOfExpMinPath = """//*[@id="min_experience"]"""
	yearsOfExpMaxPath = """//*[@id="max_experience"]"""
	jobDescPath = """/html/body/div[6]/div/div[1]/div[1]/div[4]/div[4]/div[2]/div[1]"""
	categoryPath = """//*[@id="category"]"""
	functionalAreaPath = """//*[@id="functional_area"]"""
	postJobPath = """//*[@id="submitForm"]"""
	
	driver.get(site_id)
	time.sleep(2)
	driver.find_element_by_xpath(username).send_keys(HiristId)
	driver.find_element_by_xpath(password).send_keys(HiristPwd, Keys.RETURN)
	time.sleep(1)
	driver.get(postJobSite_id)
	time.sleep(2)
	driver.find_element_by_xpath(jobTitlePath).send_keys(jobTitle)
	driver.find_element_by_xpath(locationPath).send_keys(location, Keys.DOWN, Keys.RETURN)
	Select(driver.find_element_by_xpath(yearsOfExpMinPath)).select_by_visible_text(yearsOfExperienceMin)
	Select(driver.find_element_by_xpath(yearsOfExpMaxPath)).select_by_visible_text(yearsOfExperienceMax)
	time.sleep(1)
	driver.find_element_by_xpath(jobDescPath).click()
	driver.find_element_by_xpath(jobDescPath).send_keys(jobDescription)
	time.sleep(1)
	Select(driver.find_element_by_xpath(categoryPath)).select_by_visible_text(category)
	Select(driver.find_element_by_xpath(functionalAreaPath)).select_by_visible_text(functionalArea)
	driver.find_element_by_xpath(postJobPath).click()
	print("Posted on hirist jobs")
	time.sleep(4)

main()