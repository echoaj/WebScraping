import bs4
from urllib.request import urlopen
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup

uclient = urlopen("https://en.wikipedia.org/wiki/Bill_Gates")
page_html = uclient.read()  #grabbing page html

#print(page_html)
soup = BeautifulSoup(page_html, "html.parser") #saying parse it as html file

# data = soup.find_all(class_='mw-parser-output') #'mw-parser-output'
#
# for i in data:
#     title = i.find(class_='toc').get_text() #class_='toc'
#     print(title)



#Gets all the articles in wiki page then puts the words in list
data = soup.find(class_='mw-parser-output') #'mw-parser-output'

#paragraph = data.find_all('p')[6].get_text()

words = []
for i in data.find_all('p'):
    words.append(i.get_text().split())

flatten = [k.replace(",","").replace(".","").replace(";","").replace(")","").replace(":","").replace("\"","").replace("(","") for i in words for k in i]

print("There are %d words in this article." % len(flatten))
print("Number of \"The\"s: ", flatten.count("The"))
print("Number of \"is\"s: ", flatten.count("is"))
print("Number of \"Bill\"s: ", flatten.count("Bill"))
print("Number of \"billion\"s: ", flatten.count("billion"))

