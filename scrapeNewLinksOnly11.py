from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages =set()   #create a set
def getLinks(pageUrl):
    global pages #as a global varible
    html = urlopen("http://en.wikipedia.org"+pageUrl)
    bsObj = BeautifulSoup(html,"lxml")
    for link in bsObj.findAll("a",href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages: #check whether the page link contain in pages set
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage) #add to pages set
                getLinks(newPage) #get links in that page again
getLinks("")