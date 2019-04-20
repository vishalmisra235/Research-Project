from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from time import sleep
import sys
import re
import os


alldir = []
f3 = open("filenames.txt", "r")
alldir = f3.readlines()
for i in range(0, len(alldir)):
    alldir[i] = alldir[i].replace("\n", '')
f1=open(os.path.join(r'C:\Users\Sai Krupa\Documents\Documents\CS-VI\Research_Project\GitHubRepos','allLinks.txt'), "r")
links = f1.readlines()
usr ='vishalmisra235'
pwd='vishal@1998'

options = Options()
options.add_argument("--disable-notifications")

driver = webdriver.Chrome(r"C:\Users\Sai Krupa\Downloads\chromedriver.exe",chrome_options=options)
driver.get('https://github.com/login')
print("Opened Github")

username_box= driver.find_element_by_id('login_field')
username_box.send_keys(usr)
print("Email Id Entered")

password_box = driver.find_element_by_id('password')
password_box.send_keys(pwd)
print("Password Entered")

login_box = driver.find_elements_by_class_name('btn-block')
login_box[0].click()
print("Entered Github")

c=1
for i in range(88,101):
    print(i)
    link = links[i].strip()
    print(link)
    repo = ''
    pos = link.rfind('/')
    repo = link[pos+1:] + '-master'
    print(repo)
    if repo in alldir:
        print("ok")
        driver.get(link+"/issues?q=is:issue is:closed")
        f2 = open(os.path.join(r'C:\Users\Sai Krupa\Documents\Documents\CS-VI\Research_Project\GitHubRepos'+'\\'+ repo, 'issues.txt'),"w")
        try:
            total_pages = driver.find_elements_by_tag_name('em')[0].get_attribute('data-total-pages')
        except:
            total_pages="1"
        #print("Total Pages: "+total_pages)
        #sleep(2)

        
        if int(total_pages) > 10:
            total_pages= 10

        for i in range(int(total_pages)):
            driver.get(link+"/issues?page="+str(i+1)+"&q=is:issue is:closed")
            issues = driver.find_elements_by_class_name('opened-by')
            #print(i)
            #sleep(2)
            
            issue_nos=[]
            for issue in issues:
                issue_no = ((issue.text.split())[0].split('#'))[1]
                #print(issue_no)
                issue_nos.append(issue_no)
                
            for issue in issue_nos:
                driver.get(link+"/issues/"+issue)
                open_time = driver.find_elements_by_tag_name('relative-time')[0].get_attribute('title')
                length = len(driver.find_elements_by_tag_name('relative-time'))
                close_time = driver.find_elements_by_tag_name('relative-time')[length-1].get_attribute('title')
                f2.write(issue+"\n")
                f2.write(open_time+"\n")
                f2.write(close_time+"\n")
                f2.write("\n")
                '''print("Open Time of Issue no: "+issue+" is "+open_time)
                print("Close Time of Issue no: "+issue+" is "+close_time)
                print()'''
                sleep(1)
        c=c+1
        f2.close()

f1.close()
sleep(1)
driver.quit()
