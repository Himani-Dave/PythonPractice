#Example showing the use of BeautifulSoup library for parsing HTML - Assignment 2


import urllib
from bs4 import *

url = raw_input("Enter url: ")
count = int(raw_input("Enter count: "))
position = int(raw_input("Enter position: "))
i = 0
j = 0
print "Retriving: %s" %url

while j < count:
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")

    tags = soup('a')
    third = str(tags[position-1])
    split = third.split('"')
    finallly = split[1]

    url = "https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/%s" %finallly
    j += 1

    if j == count:
        print "Last url: https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/%s" %finallly
    else:
        print "Retriving: https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/%s" %finallly
