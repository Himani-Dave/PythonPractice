import urllib
import xml.etree.ElementTree as ET

url = raw_input("Enter url:")

fhand = urllib.urlopen(url)
data = fhand.read()

stuff = ET.fromstring(data)
lst1 = stuff.findall('.//comment')
print 'Comments count:', len(lst1)

summ = 0
for each in lst1:
    num = each.find('count').text
    summ += int(num)

print 'Sum :', summ
