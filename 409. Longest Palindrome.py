import collections


def longestPalindrome(s):
    count = collections.Counter(s)
    answer = len(s)
    single = 1
    for i in count:
        if count[i] != 1 and count[i]%2 != 0:
            answer-=1
        if count[i] == 1 and single != 1:
            answer-=1
        if count[i] == 1:
            single -=1
    return answer


print(longestPalindrome("ccc"))