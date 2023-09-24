def validPalindrome(s):
    if s == s[::-1]:
        return True
    srev = s[::-1]
    first = []
    for i in range(len(s)):
        if s[i] != srev[i]:
            first.append(i)
    for i in first:
        if s.replace(s[i],'') == s.replace(s[i],'')[::-1]:
            return True
    return False





print(validPalindrome('eccer'))