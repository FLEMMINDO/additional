def findLongestChain(pairs):
    pairs = sorted(pairs, reverse=True)
    answer = 0
    pair = []
    for i in range(len(pairs)):
        if pairs[i][0] < pairs[i][1] and len(pair)==0:
            answer+=1
            pair = pairs[i]
        elif pairs[i][0] < pairs[i][1] and pair[0] > pairs[i][1]:
            answer+=1
            pair = pairs[i]
    return answer


print(findLongestChain([[-6,9],[1,6],[8,10],[-1,4],[-6,-2],[-9,8],[-5,3],[0,3]]))