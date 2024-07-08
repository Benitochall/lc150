def numWaterBottles(numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        total_num_drank = 0
        bottles_empty = 0
        bottles_full = numBottles

        while bottles_full > 0:
            # drink the bottles 
            total_num_drank += bottles_full
            bottles_empty += bottles_full
            bottles_full = 0

            # do the exchange
            bottles_full += bottles_empty // numExchange
            bottles_empty = bottles_empty % numExchange

        
        return total_num_drank
print(numWaterBottles(15,4))
