def busyStudent(startTime, endTime, queryTime):
    counter = 0
    answer = 0
    while counter != len(startTime):
        if queryTime in range(startTime[counter],endTime[counter]+1):
            answer+=1
        counter +=1
    return answer

print(busyStudent(startTime = [1,2,3], endTime = [3,2,7], queryTime = 4))