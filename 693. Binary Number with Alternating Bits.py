def hasAlternatingBits(n):
    binary_num = str(format(n, 'b'))
    for i in range(len(binary_num)-1):
        if binary_num[i] == binary_num[i+1]:
            return False
    return True



print(hasAlternatingBits(11))