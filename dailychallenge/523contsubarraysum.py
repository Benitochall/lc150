def subarraySum(nums, k):
    n = len(nums) 
    new_dict = {0: 0}

    cumulative_sum = 0
    # Iterate over all elements of the array
    for i in range(n):
        cumulative_sum += nums[i]  # Calculate the cumulative sum
        remainder = cumulative_sum % k  # Calculate the remainder
        if remainder in new_dict and i - new_dict[remainder] >= 1:
            return True
        new_dict[remainder] = i + 1  # Update the dictionary with the cumulative sum

    return False

arr = [1,2,3]
print(subarraySum(arr, 5))
