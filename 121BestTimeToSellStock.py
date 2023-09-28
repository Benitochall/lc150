def maxProfit(prices):

    min_price = prices[0]
    max_profit = 0

    # for each day we make a descion 
    # we find the max of the current max profit and the current price minus the min to find a new max profit
    # then we update the min price with the current price and the min price
    for price in prices:
        max_profit = max(max_profit, price - min_price)
        min_price = min(min_price, price)

    return max_profit

print(maxProfit([3,2,6,5,0,3]))