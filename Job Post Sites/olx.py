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
	olx()


def olx():
	OlxId = worksheet.cell(1,1).value
	OlxPwd = worksheet.cell(2,1).value
	
	typeOfJob = str(int(worksheet.cell(5,1).value))
	salaryPeriod = str(int(worksheet.cell(16,1).value))
	posType = str(int(worksheet.cell(17,1).value))
	salaryfrom = str(int(worksheet.cell(6,1).value))
	salaryto = str(int(worksheet.cell(7,1).value))
	adTitle = worksheet.cell(13,1).value
	description = worksheet.cell(24,1).value
	State = worksheet.cell(10,1).value
	City = worksheet.cell(18,1).value
	Neighbourhood = worksheet.cell(19,1).value
	phno = str(int(worksheet.cell(20,1).value))

	site_id = "https://www.olx.in/"
	postJobSite_id = "https://www.olx.in/post"
	loginPath = """//*[@id="container"]/header/div/div/div[4]/button"""
	emailPath = """/html/body/div[3]/div/div/div/button[3]"""
	usernamePath = """/html/body/div[3]/div/div/form/div/div[2]/div/div[1]/div/div/input"""
	passwordPath = """//*[@id="password"]"""
	jobPath = """//*[@id="container"]/main/div/div/div/div/div/div/ul/li[4]"""
	typeOfJobPath = """//*[@id="container"]/main/div/div/div/div/div/div/ul[2]/li[""" + typeOfJob + "]" 
	salaryPeriodPath = """//*[@id="container"]/main/div/div/div/div/div[3]/div/div[2]/div/div[1]/button[""" + salaryPeriod + "]"
	posTypePath = """//*[@id="container"]/main/div/div/div/div/div[3]/div/div[3]/div/div[1]/button[""" + posType + "]"
	salaryFromPath = """//*[@id="salary_from"]"""
	salaryToPath = """//*[@id="salary_to"]"""
	adTitlePath = """//*[@id="title"]"""
	descPath = """//*[@id="description"]"""
	StatePath = """//*[@id="State"]""" 
	cityPath = """//*[@id="City"]"""
	NeighbourhoodPath = """//*[@id="Locality"]"""
	phnoPath = """//*[@id="publicPhone"]"""
	
	driver.get(site_id)
	time.sleep(2)
	driver.find_element_by_xpath(loginPath).click()
	time.sleep(3)
	driver.find_element_by_xpath(emailPath).click()
	time.sleep(3)
	driver.find_element_by_xpath(usernamePath).send_keys(OlxId, Keys.RETURN)
	time.sleep(4)
	driver.find_element_by_xpath(passwordPath).send_keys(OlxPwd, Keys.RETURN)
	time.sleep(3)
	driver.get(postJobSite_id)
	driver.refresh()
	time.sleep(3)
	driver.find_element_by_xpath(jobPath).click()
	time.sleep(1)
	driver.find_element_by_xpath(typeOfJobPath).click()
	time.sleep(4)
	driver.find_element_by_xpath(salaryPeriodPath).click()
	driver.find_element_by_xpath(posTypePath).click()
	driver.find_element_by_xpath(salaryFromPath).send_keys(salaryfrom)
	driver.find_element_by_xpath(salaryToPath).send_keys(salaryto)
	driver.find_element_by_xpath(adTitlePath).send_keys(adTitle)
	driver.find_element_by_xpath(descPath).send_keys(description)
	Select(driver.find_element_by_xpath(StatePath)).select_by_visible_text(State)
	time.sleep(4)
	Select(driver.find_element_by_xpath(cityPath)).select_by_visible_text(City)
	time.sleep(4)
	Select(driver.find_element_by_xpath(NeighbourhoodPath)).select_by_visible_text(Neighbourhood)
	driver.find_element_by_xpath(phnoPath).send_keys(phno)
	print("Posted on olx jobs")

main()