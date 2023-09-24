def isSubsequence(s, t):
    # firstpoint = 0
    # secondpoint = 0
    # while firstpoint<len(s):
    #     if secondpoint == len(t):
    #         return False
    #     elif s[firstpoint] == t[secondpoint]:
    #         firstpoint+=1
    #         secondpoint+=1
    #     else:
    #         secondpoint +=1
    # return True
    for i in t:


print(isSubsequence(s = "ab", t = "baab"))
# Input: s = "abc", t = "ahbgdc"
# Output: true