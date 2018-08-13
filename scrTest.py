'''
from urllib.request import  urlopen
html = urlopen("http://vertspace.lk/work.html")
print(html.read())
'''

#bs4 BeautifulSoup scrape tags
from urllib.request import  urlopen
from bs4 import BeautifulSoup
html = urlopen("http://vertspace.lk/work.html")
bsObj = BeautifulSoup(html.read(),'lxml')
print(bsObj.h1)
