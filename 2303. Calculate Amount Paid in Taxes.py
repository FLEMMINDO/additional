def calculateTax(brackets, income):
    topay = 0
    temp = brackets[0][0]
    while income!=0:
        for i in brackets:
            if income >= i[0]:
                income-= temp
                topay += temp * (i[1] * 10**-2)
                temp+=1
            else:
                topay += income * (i[1] * 10**-2)
                income = 0
    return topay



print(calculateTax(brackets = [[2,7],[3,17],[4,37],[7,6],[9,83],[16,67],[19,29]], income = 18)) #ХЗ ЧЕ ЗА ЗАДАЧА, РАЗРАБ ДАУН