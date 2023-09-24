def isAnagram(s, t):
    if len(s) > len(t):
        for i in s:
            if i not in t:
                return False
            t = t.replace(i, '', 1)
        return True
    else:
        for i in t:
            if i not in s:
                return False
            s = s.replace(i, '', 1)
        return True

print(isAnagram(s = "anagram", t = "nagaram"))