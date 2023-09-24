def longestPalindrome(s):
    length = 0
    used = set()
    l = 0
    r = 0
    while l != len(s) and r != len(s):
        if s[l:r] != s[l:r][::-1]:
            r += 1
        else:
            if r - l > length:
                length = r - l
                answer = s[l:r]
    return answer

print(longestPalindrome('baaaabad'))


# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.