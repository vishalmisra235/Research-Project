from bs4 import BeautifulSoup
import urllib.request
import os
import time

f = open("links.txt", "w")
for i in range(8,18):
    html = urllib.request.urlopen("https://github.com/search?o=desc&p=" + str(i) + "&q=python&s=stars&type=Repositories")
    soup = BeautifulSoup(html, 'html.parser')
    elems = soup.find_all("a", class_="v-align-middle", href=True)
    for elem in elems:
        link = 'https://github.com' + elem['href']
        f.write(link)
        f.write("\n")
        #print(link)
        os.system("cd Documents")
        os.system("cd Documents")
        os.system("cd CS-VI")
        os.system("cd Research_Project")
        os.system("cd GithubRepos")
        os.system("git clone " + link + ".git")
        time.sleep(10)
f.close()

