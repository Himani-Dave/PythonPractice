num = []
largest = 0
smallest = 1000

while True:
    number = input("Enter a number")
    if number == "done":
        break
    else:
        try:
            number = int(number)
        except:
            print ("Invalid input")
            continue
        num.append(number)

print (num)
        
for each in num:
    if each > largest:
        largest = each
    if each < smallest:
        smallest = each
print ("Maximum is", largest)
print ("Minimum is", smallest)
