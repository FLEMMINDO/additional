def distributeCandies(candies, num_people):
    result = [0] * num_people
    i = 0
    while candies >= 0:
        result[i % num_people] += min(i + 1, candies)
        i += 1
        candies -= i
    return result



print(distributeCandies(10,3))