from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re
#first import related libraries
random.seed(datetime.datetime.now()) #set the random number generate seed with current time
def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org"+articleUrl) #path
    bsObj = BeautifulSoup(html,"lxml")
    return bsObj.find("div",{"id":"bodyContent"}).findAll("a",href = re.compile("^(/wiki/)((?!:).)*$"))
links = getLinks("/wiki/Kevin_Bacon")
#find the random article links in the page
while len(links)>0:
    newArticle = links[random.randint(0,len(links)-1)].attrs["href"]
    print(newArticle)
    links = getLinks(newArticle)