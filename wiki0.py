import bs4
from urllib.request import urlopen
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup

uclient = urlopen("https://en.wikipedia.org/wiki/0")
page_html = uclient.read()  #grabbing page html

#print(page_html)
soup = BeautifulSoup(page_html, "html.parser") #saying parse it as html file

data = soup.find(class_='mw-parser-output') #'mw-parser-output'


count0 = 0
countZero = 0

for i in data.find_all('p'):
    paragraph = i.get_text()
    for i in paragraph:
        if i == '0':
            count0 += 1

    for i in paragraph.split():
        if i == 'zero' or i == 'Zero':
            countZero += 1


print("There are %d 0s" % count0)
print("There are %d zeros" % countZero)



countUser = 0
userInput = input("Enter a word you would like to search: ")

for i in data.find_all('p'):
    paragraph = i.get_text()

    for i in paragraph.split():
        if i == userInput:
            countUser += 1

print("%d %s's found" % (countUser,userInput))