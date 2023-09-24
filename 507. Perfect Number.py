def checkPerfectNumber(num):
    divisors = []
    for i in range(1, num):
        if num%i == 0:
            divisors.append(i)
    return sum(divisors) == num





print(checkPerfectNumber(30402457))