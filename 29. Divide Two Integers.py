def divide(dividend, divisor):
    if dividend == -2147483648 and divisor == -1:
        return 2147483647
    isminus = False
    if dividend < 0 and divisor > 0:
        isminus = True
    elif dividend > 0 and divisor < 0:
        isminus = True
    dividend = abs(dividend)
    divisor = abs(divisor)
    dividend /= divisor
    if isminus:
        return int(-dividend)
    return int(dividend)


print(divide(dividend = -2147483648, divisor = -1))
# Input: dividend = 10, divisor = 3
# Output: 3
# Explanation: 10/3 = 3.33333.. which is truncated to 3.