def calPoints(operations):
    score = []
    for i in operations:
        if i[-1].isnumeric():
            score.append(int(i))
        elif i == 'C':
            score.pop(-1)
        elif i == 'D':
            score.append(score[-1]*2)
        else:
            score.append(score[-1]+score[-2])
    return sum(score)





print(calPoints(['1','C']))