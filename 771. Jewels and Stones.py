def numJewelsInStones(jewels, stones):
    answer = 0
    for i in jewels:
        answer+= stones.count(i)
    return answer

print(numJewelsInStones(jewels = "aA", stones = "aAAbbbb"))