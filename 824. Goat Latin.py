def toGoatLatin(sentence):
    tolist = sentence.split(' ')
    glas_list = ['A', 'E', 'I', 'O', 'U']
    answer = ''
    for i in range(len(tolist)):
        if tolist[i][0].upper() in glas_list:
            tolist[i] += 'ma'
        else:
            tolist[i] = tolist[i][1:len(tolist[i])] + tolist[i][0] + 'ma'
        tolist[i] += 'a'* (i+1)
        answer += tolist[i] + ' '
    answer = answer[0:len(answer)-1]
    return answer




print(toGoatLatin("yDumm"))