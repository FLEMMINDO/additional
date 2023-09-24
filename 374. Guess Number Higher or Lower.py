from statistics import mean
def guess(num, lol):
    if num > lol:
        return -1
    elif num < lol:
        return 1
    else:
        return 0

def guessNumber(n):
    number = n//2
    while guess(6, number) != 0:
        if guess(6,number) == -1:
            number += 1
        if guess(6,number) == 1:
            number -= 1
    return number





print(guessNumber(10))