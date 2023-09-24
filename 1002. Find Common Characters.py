def commonChars(words):
    s = list(words[0])
    for i in range(1, len(words)):
        todelete = []
        for letter in s:
            if letter in words[i] and words[i].count(letter) >= s.count(letter):
                pass
            elif letter in words[i] and words[i].count(letter) < s.count(letter):
                while s.count(letter) - words[i].count(letter) != todelete.count(letter):
                    todelete.append(letter)
            else:
                while todelete.count(letter)!= s.count(letter):
                    todelete.append(letter)
        for i in todelete:
            s.remove(i)
    return s




print(commonChars(["aabcdadb","cbabbbbd","bdbbcdaa","bccacaba","dddaabad","bdbddccc","bcdcdddb","dcbaccba"]))
