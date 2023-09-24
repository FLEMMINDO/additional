def addToArrayForm(num, k):
    n = ''
    for i in num:
        n+= str(i)
    n = int(n) + k
    n = str(n)
    num.clear()
    for i in n:
        num.append(int(i))
    return num

print(addToArrayForm(num = [2,7,4], k = 181))