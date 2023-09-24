from collections import Counter
def wordPattern(pattern, s):
    d = {}
    if len(pattern)!=len(s.split()):
        return False
    for i in range(len(set(pattern))):
            d[pattern[i]] = []
    for i in range(len(pattern)):
        d[pattern[i]].append(s.split()[i])
    for key in d:
        if len(set(d[key])) != 1:
            return False
        d.pop(key)
        if d[key] in d:
            return False
    return True



print(wordPattern(pattern = "abba", s = "dog dog dog dog"))