string = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'+ 'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'
string.split()
string1 = ''
for each in string:
    if ord(each) == 121:
        num = 97
        char = chr(num)
    elif ord(each) == 122:
        num = 98
        char = chr(num)
    elif each == '(' or each == ')' or each == ' ' or each =='.':
        pass
    else:
        each = ord(each) + 2
        char = chr(each)

    string1 += char

print string1
print string
