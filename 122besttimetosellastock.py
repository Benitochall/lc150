def maxProfit(prices):

    minPrice = prices[0]
    profit = 0

    # for each day we make a descion 
    # we find the max of the current max profit and the current price minus the min to find a new max profit
    # then we update the min price with the current price and the min price
    for i in range(0,len(prices)-1):
        minPrice = min(minPrice, prices[i+1])
        if (0 < (prices[i+1] - minPrice)):
            profit += prices[i+1] - minPrice
            minPrice = prices[i+1]
        

    return profit

print(maxProfit([7,6,4,3,1]))