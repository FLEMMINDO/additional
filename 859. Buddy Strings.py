def buddyStrings(s, goal):
    if len(s)!= len(goal):
        return False
    poses = []
    for i in range(len(s)):
        if s[i]!=goal[i]:
            poses.append(i)
    s = list(s)
    temp = s[poses[0]]
    s[poses[0]] = s[poses[1]]
    s[poses[1]] = temp
    s = ''.join(s)
    return s == goal



print(buddyStrings(s = "aa", goal = "aa"))