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
	naukari()
	hirist()
	instahyre()
	# indeed()
	olx()

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
	time.sleep(3)
def indeed():
	IndeedId = worksheet.cell(1,6).value
	Indeedpwd = worksheet.cell(2,6).value
	companyName = worksheet.cell(5,6).value
	jobTitle = worksheet.cell(11,6).value
	location = worksheet.cell(10,6).value
	name = worksheet.cell(13,6).value
	phnno = str(int(worksheet.cell(20,6).value))
	typeofEmp = 2
	contractType = "5"
	salaryfrom = str(int(worksheet.cell(6,6).value))
	salaryto = str(int(worksheet.cell(7,6).value))
	jobDesc = worksheet.cell(24,6).value
	# ALL SITE PATHS 
	site_id = "https://secure.indeed.com/account/login"
	username = """//*[@id="login-email-input"]"""
	password = """//*[@id="login-password-input"]"""
	signInBtn = """//*[@id="login-submit-button"]"""
	validationMsgPath = """//*[@id="login-recaptcha-message-error"]"""
	postJobSite_id = "https://employers.indeed.com/p#post-job"
	companyNamePath = """//*[@id="JobCompanyName"]"""
	jobTitlePath = """//*[@id="JobTitle"]"""
	locationPath = """//*[@id="cityOrPostalCode"]"""
	namePath = """//*[@id="AdvertiserName"]"""
	phnnoPath = """//*[@id="AdvertiserPhoneNumber"]"""
	typeofEmpPath = """//*[@id="JobEmploymentType"]"""
	contractTypePath = """//*[@id="label-checkbox-option-""" + contractType + '"]'
	salaryfromPath = """//*[@id="JobSalary1"]"""
	salarytoPath = """//*[@id="JobSalary2"]"""
	jobDescPath = """//*[@id="AppendedJobDescription-editor-content"]"""
	employerAssistAgreePath = """//*[@id="plugin-smbcommunication-EmployerAssistLegalModal-modal_box_content"]/div/div/div/div/div[2]/div[2]/div[1]/button[1]"""
	removeBannerPath = """//*[@id="plugin-pie-AddCollaboratorsTheseusModal-modal_close_button"]"""
	escapeBodyPath = "/html/body"
	applicantQualificationsPath = """//*[@id="QualificationsVisibility"]/div[1]/div[2]/div/label/div[2]"""
	skillsAssessmentsPath = """//*[@id="SkillsAssessmentVisibility"]/div[1]/div[2]/div/label/div[2]"""
	ContinuePath = """//*[@id="sheet-next-button"]"""	
	driver.get(site_id)
	ele = driver.find_element_by_xpath(username).send_keys(IndeedId)
	driver.find_element_by_xpath(password).send_keys(Indeedpwd)
	driver.find_element_by_xpath(signInBtn).click()
	driver.implicitly_wait(2)
	driver.get(postJobSite_id)
	driver.implicitly_wait(2)
	driver.find_element_by_xpath(companyNamePath).clear()
	driver.find_element_by_xpath(companyNamePath).send_keys(companyName)
	driver.find_element_by_xpath(jobTitlePath).send_keys(jobTitle, Keys.DOWN, Keys.ENTER)
	driver.find_element_by_xpath(locationPath).send_keys(location, Keys.DOWN, Keys.ENTER)
	driver.find_element_by_xpath(ContinuePath).click()
	driver.implicitly_wait(4)
	try:
		driver.find_element_by_xpath(namePath).send_keys(name)
		driver.find_element_by_xpath(phnnoPath).send_keys(phnno, Keys.TAB)
		driver.find_element_by_xpath(ContinuePath).click()
	except:
		pass
	driver.implicitly_wait(4)
	for i in range(typeofEmp):
		driver.find_element_by_xpath(typeofEmpPath).send_keys(Keys.DOWN)
	driver.implicitly_wait(2)
	driver.find_element_by_xpath(contractTypePath).click()
	driver.find_element_by_xpath(salaryfromPath).send_keys(salaryfrom)
	driver.find_element_by_xpath(salarytoPath).send_keys(salaryto)
	driver.implicitly_wait(2)
	driver.find_element_by_xpath(jobDescPath).send_keys(jobDesc)
	driver.find_element_by_xpath(ContinuePath).click()
	driver.implicitly_wait(2)
	driver.find_element_by_xpath(employerAssistAgreePath).click()
	driver.implicitly_wait(2)
	try:
		driver.find_element_by_xpath(applicantQualificationsPath).click()
		driver.find_element_by_xpath(skillsAssessmentsPath).click()
	except:
		webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
	driver.implicitly_wait(1)
	driver.find_element_by_xpath(ContinuePath).click()
	driver.implicitly_wait(3)
	driver.find_element_by_xpath(ContinuePath).click()	
	print("Posted on indeed jobs")
	driver.implicitly_wait(4)
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