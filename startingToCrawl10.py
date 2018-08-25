from urllib.request import urlopen
from bs4 import BeautifulSoup
import re #Regular Expression

html = urlopen("http://en.wikipedia.org/wiki/kevin_Bacon")
bsObj = BeautifulSoup(html,"lxml")
for link in bsObj.find("div",{"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$")):
    if 'href' in link.attrs:
        print(link.attrs['href'])