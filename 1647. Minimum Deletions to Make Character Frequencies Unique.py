def minDeletions(s):
    ans = 0
    letters = list(set(s))
    countletters = []
    for i in range(len(letters)):
        countletters.append(s.count(letters[i]))
    lneed = [i for i in range(min(countletters),len(countletters))]
    return lneed





print(minDeletions("aaabbbcc"))