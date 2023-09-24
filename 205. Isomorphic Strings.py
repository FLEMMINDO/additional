def isIsomorphic(s, t):
    return len(set(s)) == len(set(zip(s, t))) == len(set(t))

print(isIsomorphic('foo','bar'))