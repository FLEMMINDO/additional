def isPowerOfFour(n):
    count = 4
    if n == 1:
        return True
    else:
        while count < n:
            count *= 4
    if count == n:
        return True
    else:
        return False


print(isPowerOfFour(17))