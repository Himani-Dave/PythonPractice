largest = 0
smallest = 0
while True:
    num = raw_input("Enter a number: ")
    if num == "done" : 
        break
    
    elif num is int:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
            
    else:
        try:
            num 
        except:
            print "Invalid input"

print "Maximum is ", largest
print "Minimum is ", smallest
