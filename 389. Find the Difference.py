def findTheDifference(s, t):
    for i in range(len(s)):
        t = t.replace(s[i], '', 1)
    return t

print(findTheDifference(s = "a", t = "aa"))

# Input: s = "abcd", t = "abcde"
# Output: "e"
# Explanation: 'e' is the letter that was added.