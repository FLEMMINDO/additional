def generate(numRows):
    count = 1
    answer = [[1]]
    while count!=numRows:
        if len(answer)<2:
            answer.append([1,1])
            count+=1
        else:
            answer.append([1])
            for i in range(len(answer[len(answer)-2])-1):
                answer[len(answer)-1].append(answer[len(answer)-2][i]+answer[len(answer)-2][i+1])
            answer[len(answer)-1].append(1)
            count+=1
    return answer


print(generate(6))