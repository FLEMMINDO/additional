def uniqueMorseRepresentations(words):
    unique = set()
    alphabet = [['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]]
    for word in words:
        toadd = ''
        for letter in word:
            toadd += alphabet[1][alphabet[0].index(letter)]
        unique.add(toadd)
    return len(unique)

print(uniqueMorseRepresentations(words = ['a']))