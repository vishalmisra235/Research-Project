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
f8 = open("filenames.txt", "r")
alldir = f8.readlines()
for i in range(0, len(alldir)):
    alldir[i] = alldir[i].replace("\n", '')
f8.close()

f7=open(os.path.join(r'C:\Users\Sai Krupa\Documents\Documents\CS-VI\Research_Project\GitHubRepos','allLinks.txt'), "r")
links = f7.readlines()

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

f2 = open(os.path.join(r'C:\Users\Sai Krupa\Documents\Documents\CS-VI\Research_Project\GitHubRepos','all_Issues.txt'), "w")

num = 0
for i in range(0,100):
    print(i)
    link = links[i].strip()
    print(link)
    repo = ''
    pos = link.rfind('/')
    repo = link[pos+1:] + '-master'
    print(repo)
    if repo in alldir:
        try:
            num = num + 1
            driver.get(link+"/issues")
            open_issue = driver.find_elements_by_class_name('selected')
            oi = open_issue[1].text
            openiss = oi.split(" ")
            f2.write(openiss[0])
            print(openiss[0])
            f2.write("\n")
            closed_issue = driver.find_elements_by_class_name('btn-link')
            oi = closed_issue[17].text
            openiss = oi.split(" ")
            f2.write(openiss[0])
            print(openiss[0])
            f2.write("\n")
            f2.write("\n")
        except:
            print('No repo exists')
print(num)
f7.close()
f2.close()
driver.quit()
