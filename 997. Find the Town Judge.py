def findJudge(n, trust):
    trustdict = {}
    for i in range(1,n+1):
        trustdict[i] = 0
    for i in trust:
        trustdict[i[0]] = -1000
        trustdict[i[1]] += 1
    m = -10
    judge = 0
    for key,val in trustdict.items():
        if val > m and val == n-1:
            judge = key
            m = val
        elif val == m:
            return -1
    if judge != 0:
        return judge
    return -1






print(findJudge(n = 3, trust = [[1,2],[2,3]]))