def setZeroes(matrix):
    coord = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                coord.append([i,j])
    for x,y in coord:
        for plus in range(1, len(matrix)-x):
            if x+plus <= len(matrix):
                matrix[x+plus][y] = 0
        for minus in range(-1, -len(matrix) + x, -1):
            if x+minus <= 0:
                matrix[x+minus][y] = 0
        for plus in range(1, len(matrix[0])-y):
            if y+plus <= len(matrix[0]):
                matrix[x][y+plus] = 0
        for minus in range(-1, -len(matrix[0])+y, -1):
            if y+minus <= 0:
                matrix[x][y+minus] = 0
    return matrix







print(setZeroes(matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]))