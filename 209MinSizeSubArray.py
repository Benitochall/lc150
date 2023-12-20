
def minSubArrayLen(target, nums):
    if not nums:
        return 0

    left, right = 0, 0
    current_sum = 0
    min_length = 1000

    while right < len(nums):
        current_sum += nums[right]
        right += 1

        while current_sum >= target:
            min_length = min(min_length, right - left)
            current_sum -= nums[left]
            left += 1

    return min_length if min_length != 1000 else 0
        


print(minSubArrayLen(7,[2,3,1,2,4,3]))