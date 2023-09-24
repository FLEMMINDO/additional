def f(m,n,table):
    if m < 0 or n < 0:
        return 0
    if m == 0 and n == 0:
        return table[m][n]+1
    if table[m][n] == 1000:
        return 0
    table[m][n] = f(m-1,n,table) + f(m,n-1,table)
    return table[m][n]



def uniquePathsWithObstacles(obstacleGrid):
    m = len(obstacleGrid)-1
    n = len(obstacleGrid[0])-1
    return f(m,n,obstacleGrid)


#XYETA


print(uniquePathsWithObstacles([[1]]))