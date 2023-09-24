def climbStairs(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    print(b)

climbStairs(5)

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step