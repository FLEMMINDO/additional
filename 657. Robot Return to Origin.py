def judgeCircle(moves):
    return moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')


print(judgeCircle('UDLR'))