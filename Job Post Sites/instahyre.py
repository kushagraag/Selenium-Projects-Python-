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
	instahyre()

def instahyre():
	InstaHyreId = worksheet.cell(1,5).value
	InstaHyrepwd = worksheet.cell(2,5).value
	jobTitle = worksheet.cell(5,5).value
	jobFunction = worksheet.cell(11,5).value
	workExpMin = str(int(worksheet.cell(8,5).value)) + " years"
	workExpMax = str(int(worksheet.cell(9,5).value)) + " years"
	salaryMin = str(worksheet.cell(6,5).value)
	salaryMax = str(worksheet.cell(7,5).value)
	jobLocation = worksheet.cell(10,5).value
	jobDesc = worksheet.cell(24,5).value
	skills = str(int(worksheet.cell(15,5).value))
	site_id = "https://www.instahyre.com/login/"
	jobId = "https://www.instahyre.com/employer/jobs/0/0/"
	usernamePath = """//*[@id="email"]"""
	passwordPath = """//*[@id="password"]"""
	addNewJobPath = """//*[@id="jobs"]/div/div[1]/button"""
	notNowPath = """//*[@id="select-free-job-type"]"""
	jobTitlePath = """//*[@id="job-form"]/form/fieldset/div[2]/div[1]/div/input"""
	jobFunctionPath = """//*[@id="job-form"]/form/fieldset/div[2]/div[2]/div/select"""
	workExpMinPath = """//*[@id="job-form"]/form/fieldset/div[3]/div[1]/div/div/div[1]/div/select"""
	workExpMaxPath = """//*[@id="job-form"]/form/fieldset/div[3]/div[1]/div/div/div[2]/div/select"""
	salaryMinPath = """//*[@id="job-form"]/form/fieldset/div[3]/div[2]/div/div/div[1]/div/input"""
	salaryMaxPath = """//*[@id="job-form"]/form/fieldset/div[3]/div[2]/div/div/div[2]/div/input"""
	jobLocationPath = """//*[@id="preferred-location-selectized"]"""
	iframePath = """//*[@id="id-job-1-quill"]/iframe"""
	jobDescPath = """//*[@id="quill-1"]"""
	skillsPath = """//*[@id="job-form"]/form/fieldset/div[7]/div/div/div/div/li[""" + skills + "]/label/input"
	submitPath = """//*[@id="employer-jobs-save-btn"]"""
	freePostPath = """//*[@id="select-free-job-type"]"""
	driver.get(site_id)
	driver.implicitly_wait(1)
	time.sleep(1)
	for i in range(20):
		try:
			driver.find_element_by_xpath(usernamePath).send_keys(InstaHyreId)
			driver.find_element_by_xpath(passwordPath).send_keys(InstaHyrepwd, Keys.RETURN)
			driver.implicitly_wait(10)
			time.sleep(10)
			break
		except:
			driver.implicitly_wait(1)
			time.sleep(1)
			pass
	print("1")
	try:
		driver.find_element_by_xpath(notNowPath).click()
		driver.implicitly_wait(3)
		time.sleep(3)
	except:
		driver.implicitly_wait(1)
		time.sleep(1)
		pass
	print("2")
	driver.get(jobId)
	driver.implicitly_wait(5)
	time.sleep(3) # seconds
	time.sleep(4)
	for i in range(20):
		try:	
			driver.find_element_by_xpath(addNewJobPath).click()
			break
		except:
			driver.implicitly_wait(2)
			time.sleep(2)
			pass
	driver.implicitly_wait(3)
	time.sleep(3) # seconds
	driver.find_element_by_xpath(jobTitlePath).send_keys(jobTitle)
	Select(driver.find_element_by_xpath(jobFunctionPath)).select_by_visible_text(jobFunction)
	Select(driver.find_element_by_xpath(workExpMinPath)).select_by_visible_text(workExpMin)
	driver.implicitly_wait(1)
	time.sleep(3)
	Select(driver.find_element_by_xpath(workExpMaxPath)).select_by_visible_text(workExpMax)
	driver.find_element_by_xpath(salaryMinPath).send_keys(salaryMin)
	driver.find_element_by_xpath(salaryMaxPath).send_keys(salaryMax)
	driver.find_element_by_xpath(jobLocationPath).send_keys(Keys.BACKSPACE, jobLocation, Keys.ENTER)
	# for job description
	iframe = driver.find_element_by_xpath(iframePath)
	driver.switch_to.frame(iframe)
	driver.find_element_by_xpath(jobDescPath).click()
	driver.find_element_by_xpath(jobDescPath).send_keys(jobDesc)
	driver.switch_to.default_content()
	#back to normal
	driver.find_element_by_xpath(skillsPath).click()
	driver.find_element_by_xpath(submitPath).click()
	driver.implicitly_wait(2)
	time.sleep(3)
	try:
		driver.find_element_by_xpath(freePostPath).click()
	except:
		pass
	print("Posted on InstaHyre jobs")
	driver.implicitly_wait(4)
	time.sleep(3)def instahyre():
	InstaHyreId = worksheet.cell(1,5).value
	InstaHyrepwd = worksheet.cell(2,5).value
	jobTitle = worksheet.cell(5,5).value
	jobFunction = worksheet.cell(11,5).value
	workExpMin = str(int(worksheet.cell(8,5).value)) + " years"
	workExpMax = str(int(worksheet.cell(9,5).value)) + " years"
	salaryMin = str(worksheet.cell(6,5).value)
	salaryMax = str(worksheet.cell(7,5).value)
	jobLocation = worksheet.cell(10,5).value
	jobDesc = worksheet.cell(24,5).value
	skills = str(int(worksheet.cell(15,5).value))
	site_id = "https://www.instahyre.com/login/"
	jobId = "https://www.instahyre.com/employer/jobs/0/0/"
	usernamePath = """//*[@id="email"]"""
	passwordPath = """//*[@id="password"]"""
	addNewJobPath = """//*[@id="jobs"]/div/div[1]/button"""
	notNowPath = """//*[@id="select-free-job-type"]"""
	jobTitlePath = """//*[@id="job-form"]/form/fieldset/div[2]/div[1]/div/input"""
	jobFunctionPath = """//*[@id="job-form"]/form/fieldset/div[2]/div[2]/div/select"""
	workExpMinPath = """//*[@id="job-form"]/form/fieldset/div[3]/div[1]/div/div/div[1]/div/select"""
	workExpMaxPath = """//*[@id="job-form"]/form/fieldset/div[3]/div[1]/div/div/div[2]/div/select"""
	salaryMinPath = """//*[@id="job-form"]/form/fieldset/div[3]/div[2]/div/div/div[1]/div/input"""
	salaryMaxPath = """//*[@id="job-form"]/form/fieldset/div[3]/div[2]/div/div/div[2]/div/input"""
	jobLocationPath = """//*[@id="preferred-location-selectized"]"""
	iframePath = """//*[@id="id-job-1-quill"]/iframe"""
	jobDescPath = """//*[@id="quill-1"]"""
	skillsPath = """//*[@id="job-form"]/form/fieldset/div[7]/div/div/div/div/li[""" + skills + "]/label/input"
	submitPath = """//*[@id="employer-jobs-save-btn"]"""
	freePostPath = """//*[@id="select-free-job-type"]"""
	driver.get(site_id)
	driver.implicitly_wait(1)
	time.sleep(1)
	for i in range(20):
		try:
			driver.find_element_by_xpath(usernamePath).send_keys(InstaHyreId)
			driver.find_element_by_xpath(passwordPath).send_keys(InstaHyrepwd, Keys.RETURN)
			driver.implicitly_wait(10)
			time.sleep(10)
			break
		except:
			driver.implicitly_wait(1)
			time.sleep(1)
			pass
	print("1")
	try:
		driver.find_element_by_xpath(notNowPath).click()
		driver.implicitly_wait(3)
		time.sleep(3)
	except:
		driver.implicitly_wait(1)
		time.sleep(1)
		pass
	print("2")
	driver.get(jobId)
	driver.implicitly_wait(5)
	time.sleep(3) # seconds
	time.sleep(4)
	for i in range(20):
		try:	
			driver.find_element_by_xpath(addNewJobPath).click()
			break
		except:
			driver.implicitly_wait(2)
			time.sleep(2)
			pass
	driver.implicitly_wait(3)
	time.sleep(3) # seconds
	driver.find_element_by_xpath(jobTitlePath).send_keys(jobTitle)
	Select(driver.find_element_by_xpath(jobFunctionPath)).select_by_visible_text(jobFunction)
	Select(driver.find_element_by_xpath(workExpMinPath)).select_by_visible_text(workExpMin)
	driver.implicitly_wait(1)
	time.sleep(3)
	Select(driver.find_element_by_xpath(workExpMaxPath)).select_by_visible_text(workExpMax)
	driver.find_element_by_xpath(salaryMinPath).send_keys(salaryMin)
	driver.find_element_by_xpath(salaryMaxPath).send_keys(salaryMax)
	driver.find_element_by_xpath(jobLocationPath).send_keys(Keys.BACKSPACE, jobLocation, Keys.ENTER)
	# for job description
	iframe = driver.find_element_by_xpath(iframePath)
	driver.switch_to.frame(iframe)
	driver.find_element_by_xpath(jobDescPath).click()
	driver.find_element_by_xpath(jobDescPath).send_keys(jobDesc)
	driver.switch_to.default_content()
	#back to normal
	driver.find_element_by_xpath(skillsPath).click()
	driver.find_element_by_xpath(submitPath).click()
	driver.implicitly_wait(2)
	time.sleep(3)
	try:
		driver.find_element_by_xpath(freePostPath).click()
	except:
		pass
	print("Posted on InstaHyre jobs")
	driver.implicitly_wait(4)
	time.sleep(3)

main()


//*[@id="side"]/div[1]/div/label/div/div[2]