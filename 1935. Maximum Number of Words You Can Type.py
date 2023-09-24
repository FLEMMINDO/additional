def canBeTypedWords(text, brokenLetters):
    text = text.split()
    ans = 0
    for word in text:
        ans += 1
        for letter in brokenLetters:
            if letter in word:
                ans -= 1
                break
    return ans



print(canBeTypedWords(text = "hello world", brokenLetters = "ad"))