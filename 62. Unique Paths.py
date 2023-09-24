def f(x,y,table):
    if x < 0 or y < 0:
        return 0
    if table[x][y] != -1:
        return table[x][y]
    table[x][y] = f(x-1,y,table)+f(x,y-1,table)
    return table[x][y]

def uniquePaths(m, n):
    table = [[-1 for _ in range(n)] for _ in range(m)]
    m-=1
    n-=1
    table[0][0] = 1
    ans = f(m,n,table)
    return ans



print(uniquePaths(3,7))