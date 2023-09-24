def numRookCaptures(board):
    x = 0
    y = 0
    for i in board:
        if i.count('R') == 1:
            x = board.index(i)
            y = i.index('R')
            break
    ans = 0
    toreturn = [x, y]
    while x != len(board) - 1:
        x += 1
        if board[x][y] == 'B':
            break
        if board[x][y] == 'p':
            ans += 1
            break
    x = toreturn[0]
    while x != 0:
        x -= 1
        if board[x][y] == 'B':
            break
        if board[x][y] == 'p':
            ans += 1
            break
    x = toreturn[0]
    while y != len(board[0]) - 1:
        y += 1
        if board[x][y] == 'B':
            break
        if board[x][y] == 'p':
            ans += 1
            break
    y = toreturn[1]
    while y != 0:
        y -= 1
        if board[x][y] == 'B':
            break
        if board[x][y] == 'p':
            ans += 1
            break
    return ans







print(numRookCaptures([[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]))