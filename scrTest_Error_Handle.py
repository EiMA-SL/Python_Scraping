#Exeption Handling-Page Not Found/Server Not
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

try:
    html = urlopen("http://vertspace.lk/work.html")
except HTTPError as e:
    print(e)
    #Return Null,Break or Other
except URLError as e:
    print("The server could not be found!")
else:
    #Continues
    print("It worked!")