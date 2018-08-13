from urllib.request import urlopen
from urllib.request import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(),'lxml')
        title = bsObj.body.D1
    except AttributeError as e:
        return None
    return title

title = getTitle("http://vertspace.lk/work.html")
if title== None:
    print("Title could not be found")
else:
    print(title)