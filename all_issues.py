from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from time import sleep
import sys
import re
import os

f1=open(os.path.join(r'F:\Research Project','allLinks.txt'), "r")

usr ='vishalmisra235'
pwd='vishal@1998'

options = Options()
options.add_argument("--disable-notifications")

driver = webdriver.Chrome(r"C:\Users\Vishal\Desktop\Old HP Laptop data\chromedriver_win32\chromedriver.exe",chrome_options=options)
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

f2 = open(os.path.join(r'F:\Research Project','all_Issues.txt'), "w")

c=0
for link in f1:
    try:
        if(c==100):
            break
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
        c=c+1
    except:
        print('No repo exists')
    

f1.close()
f2.close()
driver.quit()
