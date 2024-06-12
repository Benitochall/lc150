'''
Idea so we can build an array of minimum coins need to make that position in the array
so array[5] will hold the value of the minimum coins needed to make 5
array[0] will always be 0 because we need 0 coins to make 0
then starting with the smallest demonination we go through the array from array[coin] to array[amount]
and we update the value of array[i] to be the minimum of array[i-coin] + 1 and array[i]
this is the current smallest number of coins needed to make that amount or the number of coins needed to make that amount - coin and then add that current coin.
this effectively builds the array of minimum coins needed to make that amount
'''
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        array = [amount +1] * (amount+1)
        array[0] = 0
        for coin in coins:
            for i in range(coin,len(array)):
                array[i] = min(array[i-coin] +1,array[i])
        if array[amount] < (amount +1):
            return array[amount]
        else: 
            return -1
