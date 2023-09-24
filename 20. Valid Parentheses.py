def isValid(s):
    firsttype = '()'
    secondtype = '[]'
    thirdtype = '{}'
    for i in range(len(s)//2):
        s = s.replace(firsttype, '').replace(secondtype, '').replace(thirdtype, '')
    if len(s) == 0:
       print(True)
    else:
        print(False)

isValid("([])")