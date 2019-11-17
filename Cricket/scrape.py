from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import csv

outfile = open('jujama_attendees.csv', 'w+')
outfile_csv_writer = csv.writer(outfile)

firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference('permissions.default.image', 2)

driver = webdriver.Firefox(firefox_profile=firefox_profile)
driver.get('https://connect.jujama.com/EduTECH-Asia-2019')
driver.implicitly_wait(10)

# Login workflow
username = driver.find_element_by_name('txtUserName')
password = driver.find_element_by_name('txtPassword')
submit_btn = driver.find_element_by_name('btnSubmit')
username.send_keys('hari@saleswhale.com')
password.send_keys('cricket123')
submit_btn.click()

# Navigate and get attendee
wait = WebDriverWait(driver, 30)
profile_link = wait.until(EC.element_to_be_clickable((By.ID, 'rptMenu_hlnkTabName_1')))
profile_link.click()

# Get info
names = driver.find_elements_by_xpath("//a[starts-with(@id,'cphMain_ucPeople_dlPeople_hlnkPersonName')]")
job_titles = driver.find_elements_by_xpath("//span[starts-with(@id,'cphMain_ucPeople_dlPeople_lblJobTitle')]")
companies = driver.find_elements_by_xpath("//a[starts-with(@id,'cphMain_ucPeople_dlPeople_hlnkCompanyName')]")
countries = driver.find_elements_by_xpath("//span[starts-with(@id,'cphMain_ucPeople_dlPeople_lblCountry')]")
info_list = list(zip(names, job_titles, companies, countries))
# Process info
for info in info_list:
    info_text_tuple = [elem.text for elem in info]
    print(info_text_tuple)
    outfile_csv_writer.writerow(info_text_tuple)

#Navigate
for page in range(2,241):
    wait.until(EC.text_to_be_present_in_element_value((By.NAME,'ctl00$cphMain$CustomPager1$txtPage'), str(page - 1)))
    page_input = driver.find_element_by_name('ctl00$cphMain$CustomPager1$txtPage')
    page_input.clear()
    page_input.send_keys(page)
    page_submit = wait.until(EC.element_to_be_clickable((By.ID, 'cphMain_CustomPager1_lnkGotopages')))
    page_submit = wait.until(EC.element_to_be_clickable((By.ID, 'cphMain_CustomPager1_lnkGotopages')))
    page_submit.click()
    time.sleep(5)

    for page in range (242,357):
     wait.until(EC.text_to_be_present_in_element_value((By.NAME,'ctl00$cphMain$CustomPager1$txtPage'), str(page - 1)))
    page_input = driver.find_element_by_name('ctl00$cphMain$CustomPager1$txtPage')
    page_input.clear()
    page_input.send_keys(page)
    page_submit = wait.until(EC.element_to_be_clickable((By.ID, 'cphMain_CustomPager1_lnkGotopages')))
    page_submit = wait.until(EC.element_to_be_clickable((By.ID, 'cphMain_CustomPager1_lnkGotopages')))
    page_submit.click()
    time.sleep(15)
    names = driver.find_elements_by_xpath("//a[starts-with(@id,'cphMain_ucPeople_dlPeople_hlnkPersonName')]")
    job_titles = driver.find_elements_by_xpath("//span[starts-with(@id,'cphMain_ucPeople_dlPeople_lblJobTitle')]")
    companies = driver.find_elements_by_xpath("//a[starts-with(@id,'cphMain_ucPeople_dlPeople_hlnkCompanyName')]")
    countries = driver.find_elements_by_xpath("//span[starts-with(@id,'cphMain_ucPeople_dlPeople_lblCountry')]")
    info_list = list(zip(names, job_titles, companies, countries))
    # Process info
    for info in info_list:
        info_text_tuple = [elem.text for elem in info]
        print(info_text_tuple)
        outfile_csv_writer.writerow(info_text_tuple)

logout = driver.find_element_by_id('hlnkLogout')
logout.click()

driver.close()
driver.quit()
outfile.close()