def countPrimes(n):
    answerarr = [i for i in range(n+1)]
    count = 2
    answerarr[1] = 0
    while count <= n**0.5:
        if answerarr[count]!=0:
            j = count**2
            while j <= n:
                answerarr[j] = 0
                j += count
            count+=1
    answer = [i for i in answerarr if answerarr[i] != 0]
    return len(answer)


print(countPrimes(10))

# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.