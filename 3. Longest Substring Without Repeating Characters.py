def lengthOfLongestSubstring(s):
    length = 0
    used = set()
    l = 0
    r = 0
    while l != len(s) and r != len(s):
        if s[r] in used:
            used.remove(s[l])
            l += 1
        else:
            used.add(s[r])
            r += 1
            if r - l > length:
                length = r - l
    return length

print(lengthOfLongestSubstring('abcabcbb'))

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.