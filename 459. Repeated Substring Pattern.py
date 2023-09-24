def repeatedSubstringPattern(s):
    return len(s)//len(set(s))


print(repeatedSubstringPattern("abcbac"))