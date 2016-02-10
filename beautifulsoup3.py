#Example showing the use of BeautifulSoup library for parsing HTML - Assignment 2


import urllib
from bs4 import BeautifulSoup

def getNthLink(url, n):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    return tags[n-1]

url = raw_input("Enter url: ")
count = int(raw_input("Enter count: "))
position = int(raw_input("Enter position: "))

print "Retriving: %s" %url

for i in xrange(count):
    tag = getNthLink(url,position)
    url_bef = tag.get('href')
    url = "https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/%s" %url_bef
    if i == count - 1:
        print "Last url: %s" %url
    else:
        print "Retriving: %s" %url
