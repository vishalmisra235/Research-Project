from bs4 import BeautifulSoup
import urllib.request
import os
import time

f = open("links.txt", "w")
for i in range(1,10):
    html = urllib.request.urlopen("https://github.com/search?o=desc&p=" + str(i) + "&q=python&s=stars&type=Repositories")
    soup = BeautifulSoup(html, 'html.parser')
    doc = soup.find_all("div", class_="text-gray flex-auto min-width-0")
    elems = soup.find_all("a", class_="v-align-middle", href=True)
    for elem in elems:
        link = 'https://github.com' + elem['href']
        lang = driver.find_elements_by_xpath('//*[@id="js-pjax-container"]/div/div[3]/div/ul/li/div[2]/div[1]')
        print(lang)
        f.write(link)
        f.write("\n")
        #print(link)
f.close()

