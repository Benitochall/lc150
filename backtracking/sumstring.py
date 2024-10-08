def combinationsum(nums, target):

    sol = []

    def backtrack(i, array, total):
        if sum(array) == target:
            sol.append(array[:])
            return
        if i >= len(nums) or total > target:
            return

       
        array.append(nums[i])
        backtrack(i,array, total + nums[i])
        array.pop()
        backtrack(i+1, array, total)
        


        
    backtrack(0,[],0)
    print(sol)

    pass



combinationsum([2,5,6,9],9)