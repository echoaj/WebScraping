from urllib.request import urlopen
from bs4 import BeautifulSoup

while True:
    wikiPage = input("Enter a wikipedia page: ")
    wikiPage.replace(' ', '_')

    try:
        uclient = urlopen("https://en.wikipedia.org/wiki/" + wikiPage)
        page_html = uclient.read()                          #grabbing page html
    except:
        print("Page Not Found\n")
    else:
        print("Page Found\n")
        break

soup = BeautifulSoup(page_html, "html.parser")      #saying parse it as html file
data = soup.find(class_='mw-parser-output')         #'mw-parser-output'

while True:
    countUser = 0
    userInput = input("Enter a word you would like to search: ")
    if userInput == 'q':
        break

    for i in data.find_all('p'):
        paragraph = i.get_text()

        for i in paragraph.split():
            if i == userInput:
                countUser += 1

    print("%d %s's found" % (countUser,userInput) + '\n')
