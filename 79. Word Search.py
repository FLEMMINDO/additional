def exist(board, word):
    x = 0
    y = 0
    xmax = len(board[0])
    ymax = len(board)
    count = 0
    startpoint = []
    while y != ymax:
        while x != xmax:
            if board[x][y] == word[0] and (board[x+1][y] == word[1] or board[x][y+1] == word[1]):
                startpoint.append(x)
                startpoint.append(y)
                x+=1
            else:
                x+=1
        y+=1
        x = 0

    if startpoint == []:
        return False
    return startpoint


print(exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"))
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true