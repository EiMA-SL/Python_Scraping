from urllib.request import  urlopen
html = urlopen("http://vertspace.lk/work.html")
print(html.read())