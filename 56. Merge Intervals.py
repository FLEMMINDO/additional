def merge(intervals):
    ans = []
    if len(intervals) == 1:
        return intervals
    for i in range(0,len(intervals)-1,2):
        if intervals[i][1] >= intervals[i+1][0]:
            ans.append([intervals[i][0],intervals[i+1][1]])
        else:
            ans.append(intervals[i])
            ans.append(intervals[i+1])
    return ans







print(merge([[1,3]]))