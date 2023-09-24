def myAtoi(s):
    ans = ''
    isneg = False
    for i in s:
        if i == '-':
            isneg = True
        elif i.isdigit():
            ans += i
        if i.isalpha():
            break
    ans = ans.format(32)
    if isneg:
        return -int(ans)
    return int(ans)

print(myAtoi("-91283472332"))