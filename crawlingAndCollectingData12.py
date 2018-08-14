from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages =set()   #create a set
def getLinks(pageUrl):
    global pages #as a global varible
    html = urlopen("http://en.wikipedia.org"+pageUrl)
    bsObj = BeautifulSoup(html,"lxml")
    try:
        print("H1: ", bsObj.h1.get_text())
        print("1st paragraph:\n",bsObj.find(id = "mw-content-text").findAll("p")[0])
        print("Edit Link : ",bsObj.find(id="ca-edit").find("span").find("a").attrs['href'])
    except AttributeError:
        print("This page is missing something!")
    for link in bsObj.findAll("a",href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages: #check whether the page link contain in pages set
                newPage = link.attrs['href']
                print('----------------------------------\n'+newPage)
                #print(newPage)
                pages.add(newPage) #add to pages set
                getLinks(newPage) #get links in that page again
getLinks("")