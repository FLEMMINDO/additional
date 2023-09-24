def convert(s, numRows):
    l = [[] for _ in range(numRows)]
    mover = 0
    letters = 0
    reachedEnd = False
    while letters!=len(s):
        if reachedEnd == False or numRows <= 1:
            l[mover].append(s[letters])
            mover+=1
            letters+=1
            if mover == len(l):
                reachedEnd = True
                mover-=1
        else:
            mover-=1
            l[mover].append(s[letters])
            letters+=1
            if mover == 0:
                reachedEnd = False
                mover+=1
    answer = ''
    for i in l:
        for l in i:
            answer+= l
    return answer



print(convert(s = "ABC", numRows = 1))