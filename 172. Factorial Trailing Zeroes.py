def trailingZeroes(n):
    # nres = 1
    # for i in range(1, n+1):
    #     nres *= i
    # nres = str(nres)
    # nres = nres[::-1]
    # ans = 0
    # for i in nres:
    #     if i == '0':
    #         ans+=1
    #     else:
    #         return ans
    # MINE
    co = 0
    while n > 0:
        co += n // 5
        n //= 5
    return co


print(trailingZeroes(5))