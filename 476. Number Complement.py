def findComplement(num):
    num = "{0:b}".format(num)
    ans = ''
    for i in num:
        if i == '1':
            ans += '0'
        else:
            ans += '1'
    return int(ans, 2)

print(findComplement(1))