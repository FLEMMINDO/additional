def numberOfLines(widths, s):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    linecount = 1
    lineval = 0
    for letter in s:
        if lineval+widths[alphabet.index(letter)] <= 100:
            lineval += widths[alphabet.index(letter)]
        else:
            lineval = 0
            lineval += widths[alphabet.index(letter)]
            linecount+=1
    return [linecount,lineval]


print(numberOfLines(widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], s = "bbbcccdddaaa"))