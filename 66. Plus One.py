def plusOne(digits):
    # singledg = ''
    # for i in digits:
    #     singledg += str(i)
    # del digits[:]
    # singledg = int(singledg)
    # singledg +=1
    # for i in str(singledg):
    #     digits.append(int(i))
    # print(digits)
    digits = [str(i) for i in digits]
    s = ''.join(digits)
    a = int(s) + 1
    l = list(str(a))
    l = [int(i) for i in l]
    print(l)
plusOne([1,2,3])