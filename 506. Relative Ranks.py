def findRelativeRanks(score):
    arr = ['' for _ in range(len(score))]
    for i in range(len(score)):
        morethan = 0
        for j in range(len(score)):
            if i == j:
                pass
            if score[i] > score[j]:
                morethan +=1
        if len(score)-morethan == 1:
            arr[i] = 'Gold Medal'
        elif len(score)-morethan == 2:
            arr[i] = 'Silver Medal'
        elif len(score)-morethan == 3:
            arr[i] = 'Bronze Medal'
        else:
            arr[i] = str(len(score)-morethan)
    return arr








print(findRelativeRanks(score = [10,3,8,9,4]))