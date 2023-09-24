def isHappy(n):
    used = []
    while n!=1:
        tmp = 0
        while n>0:
            dg = n%10

            tmp += dg**2
            n = n//10
        if tmp in used:
            return False
        else:
            used.append(tmp)
        n = tmp
    return True




print(isHappy(7))