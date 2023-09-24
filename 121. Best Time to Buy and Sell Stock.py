def maxProfit(prices):
    maxes = []
    if len(prices)%2==0:
        minf = min(prices[0:len(prices)//2])
        maxf = max(prices[prices.index(minf):len(prices)//2])
        maxes.append(maxf-minf)
        minf = min(prices[len(prices)//2:len(prices)])
        maxf = max(prices[prices.index(minf):len(prices)//2])
        maxes.append(maxf-minf)
        minf = min(prices[0:len(prices)//2])
        maxf = max(prices[prices.index(minf):len(prices)])
        maxes.append(maxf-minf)
        return max(maxes)



print(maxProfit([7,3,4,8,1,6]))