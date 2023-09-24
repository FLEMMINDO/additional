def maxRepeating(sequence, word):
    maxcount = 0
    for i in range(1, len(sequence)+1):
        tocheck = word*i
        if tocheck in sequence:
            maxcount = i
    return maxcount

print(maxRepeating(sequence = "ababcab", word = "ab"))


# temp = -100
    # counter = 0
    # count = 0
    # while counter!= len(sequence):
    #     if sequence[counter:counter+len(word)] == word:
    #         for j in range(counter, len(sequence)-1, len(word)):
    #             if sequence[j:j+len(word)] == word:
    #                 count +=1
    #             counter = j
    #     temp = max(temp,count)
    #     count = 0
    #     counter+=1
    # return temp