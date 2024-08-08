
def maxProfit(prices):

    # the idea behind

    m = 0

    i= 0 # day that we buy
    j = 1 # day that we sell

    while i < len(prices):
        if prices[j] - prices[i] > 0:
            m = max(prices[j] - prices[i], m)
        else:
            i = j
        j+=1

    return m


if __name__ == '__main__':
    prices = [10,1,5,6,7,1]

    maxProfit(prices)

