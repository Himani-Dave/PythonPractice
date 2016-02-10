#Example showing the use of BeautifulSoup library for parsing HTML - Assignment 1


import urllib
from bs4 import *

url = "http://python-data.dr-chuck.net/comments_237729.html "

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup('span')

summ = 0

for tag in tags:
    summ = summ + int(tag.contents[0])

print summ
