def hammingWeight(n):
    count = 0
    while n != 0:
        if n & 1 == 1:
            count += 1
        n = n >> 1
    return count

print(hammingWeight(n = 11111111111111111111111111111101))
# Input: n = 11111111111111111111111111111101
# Output: 31
# Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.