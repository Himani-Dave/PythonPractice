#Example showing the use of BeautifulSoup library for parsing HTML


import urllib
from bs4 import *

url = raw_input("Enter url : ")

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup('a')

for tag in tags:
    print tag.get('href', None)
