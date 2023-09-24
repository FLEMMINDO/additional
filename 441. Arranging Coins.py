def arrangeCoins(n):
    count = 1
    while n/count > count:
        count += 1
        n = n/count
    return count


print(arrangeCoins(8))
# Input: n = 8
# Output: 3
# Explanation: Because the 4th row is incomplete, we return 3.