def hammingDistance(x, y):
    x = "{0:b}".format(x)
    y = "{0:b}".format(y)
    count = 0
    if len(x) > len(y):
        while len(y) != len(x):
            y = '0' + y
    else:
        while len(x) != len(y):
            x = '0' + x
    for i in range(len(x)):
        if x[i] != y[i]:
            count+=1
    return count

print(hammingDistance(3,1))