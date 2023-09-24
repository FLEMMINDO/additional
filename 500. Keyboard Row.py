def findWords(words):
    set1 = {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'}
    set2 = {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'}
    set3 = {'z', 'x', 'c', 'v', 'b', 'n', 'm'}
    res = []
    for i in words:
        wordset = set(i.lower())
        if wordset.issubset(set1) or wordset.issubset(set2) or wordset.issubset(set3):
            res.append(i)
    return res




print(findWords(words = ["Hello","Alaska","Dad","Peace"]))