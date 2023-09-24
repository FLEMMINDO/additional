def addDigits(num):
    ans = str(num)
    while len(ans)!=1:
        count = 0
        for i in ans:
            count += int(i)
        ans = str(count)
    return int(ans)

print(addDigits(38))

# Input: num = 38
# Output: 2
# Explanation: The process is
# 38 --> 3 + 8 --> 11
# 11 --> 1 + 1 --> 2
# Since 2 has only one digit, return it.