import urllib
import json

url = raw_input("Enter url:")

fhand = urllib.urlopen(url)
data = fhand.read()

info = json.loads(data)

count = 0
summ = 0
for each in info['comments']:
    count += 1
    summ += each['count']

print "Count :", count
print "Sum: ", summ
