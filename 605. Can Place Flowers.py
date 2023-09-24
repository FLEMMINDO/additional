def canPlaceFlowers(flowerbed, n):
    canPlace = 0
    if len(flowerbed) == 1 and flowerbed[0] == 0 and n == 1:
        return True
    elif len(flowerbed) == 1 and flowerbed[0] == 1 and n>=1:
        return False
    elif len(flowerbed) == 1 and flowerbed[0] == 1 and n == 0:
        return True
    for i in range(len(flowerbed)):
        if i == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
            flowerbed[i] = 1
            canPlace+=1
        if i == len(flowerbed)-1 and flowerbed[i-1] == 0 and flowerbed[i] == 0:
            flowerbed[i] = 1
            canPlace += 1
        if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
            flowerbed[i] = 1
            canPlace += 1
    if canPlace >= n:
        return True
    return False





print(canPlaceFlowers(flowerbed = [1,0,0,0,1,0,0], n = 2))