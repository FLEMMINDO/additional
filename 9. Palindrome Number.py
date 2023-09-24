def isPalindrome(x):
    ans = str(x)
    if ans.startswith('-'):
        return False
    elif ans[::-1] == ans:
        return True
    else:
        return False

print(isPalindrome(123))


# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.