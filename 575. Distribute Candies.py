def distributeCandies(candyType):
    caneat = len(candyType) // 2
    s = set(candyType)
    if len(s) >= caneat:
        return caneat
    else:
        return len(s)



print(distributeCandies([6,6,6,6,6,6,6,6,6,6]))