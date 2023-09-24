def kWeakestRows(mat, k):
    ans = []
    for i in range(k):
        ans.append(mat.index(min(mat)))
        mat[mat.index(min(mat))][0] = 9999
    return ans


print(kWeakestRows(mat =
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]],
k = 3))