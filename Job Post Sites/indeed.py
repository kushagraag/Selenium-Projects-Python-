import time
from selenium import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains


#path for chromedriver, replace \ with \\ everywhere in address, chromedriver version must match with installed chrome on device
chromedriver = 'D:\\truelancer selenium python\\chromedriver_win32\\chromedriver.exe'
driver=webdriver.Chrome(executable_path=chromedriver)

# REFER TO READMEE FILE FOR INSTRUCTIONS ON HOW TO ENTER VALUES
IndeedId = "eovnstd1@protonmail.com"
Indeedpwd = "Qwerty12345"

companyName = "sample job1"
jobTitle = "Programmer Analyst"
location = "Delhi"
name = """anony"""
phnno = """9876543211"""
typeofEmp = 2
contractType = "5" 
salaryfrom = "10000"
salaryto = "50000"
jobDesc = "qwertyuuuiopasdfghjklzxcvbnmqwertyuiosdfghjklzxcvbnmwertyuio"

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
# dontoptimizePath = """//*[@id="uniqueId1"]"""
# nothnxPath = """//*[@id="trial-modal-free-link"]"""


driver.get(site_id)
ele = driver.find_element_by_xpath(username).send_keys(IndeedId)
driver.find_element_by_xpath(password).send_keys(Indeedpwd)
driver.find_element_by_xpath(signInBtn).click()
time.sleep(2)
driver.get(postJobSite_id)
time.sleep(2)
driver.find_element_by_xpath(companyNamePath).clear()
driver.find_element_by_xpath(companyNamePath).send_keys(companyName)
driver.find_element_by_xpath(jobTitlePath).send_keys(jobTitle, Keys.DOWN, Keys.ENTER)
driver.find_element_by_xpath(locationPath).send_keys(location, Keys.DOWN, Keys.ENTER)
driver.find_element_by_xpath(ContinuePath).click()
time.sleep(4)
try:
	driver.find_element_by_xpath(namePath).send_keys(name)
	driver.find_element_by_xpath(phnnoPath).send_keys(phnno, Keys.TAB)
	driver.find_element_by_xpath(ContinuePath).click()
except:
	pass
time.sleep(4)
for i in range(typeofEmp):
	driver.find_element_by_xpath(typeofEmpPath).send_keys(Keys.DOWN)
time.sleep(2)
driver.find_element_by_xpath(contractTypePath).click()
driver.find_element_by_xpath(salaryfromPath).send_keys(salaryfrom)
driver.find_element_by_xpath(salarytoPath).send_keys(salaryto)
time.sleep(2)
driver.find_element_by_xpath(jobDescPath).send_keys(jobDesc)
driver.find_element_by_xpath(ContinuePath).click()
time.sleep(2)
driver.find_element_by_xpath(employerAssistAgreePath).click()
time.sleep(2)
try:
	driver.find_element_by_xpath(applicantQualificationsPath).click()
	driver.find_element_by_xpath(skillsAssessmentsPath).click()
except:
	webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
time.sleep(1)
driver.find_element_by_xpath(ContinuePath).click()
time.sleep(3)
driver.find_element_by_xpath(ContinuePath).click()