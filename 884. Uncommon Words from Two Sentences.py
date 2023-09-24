def uncommonFromSentences(s1, s2):
    s1 = s1.split()
    s2 = s2.split()
    uncommon = []
    for i in s1:
        if s1.count(i) == 1 and i not in s2:
            uncommon.append(i)
    for j in s2:
        if s2.count(j) == 1 and j not in s1:
            uncommon.append(j)
    return uncommon




print(uncommonFromSentences(s1 = "apple apple", s2 = "banana"))
