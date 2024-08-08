def subsets(s):
    # backtracking

    sol = []

    def backtrack(arr, index):
        # check to see if the current is a solution
        sol.append(arr[:])

        # Explore all subsets that include s[index]
        for i in range(index, len(s)):
            arr.append(s[i])
            backtrack(arr, i + 1) # recursivly call on that new solution
            arr.pop() # go back to the old solution and try a differnt path

    
    backtrack([],0)
    return sol




if __name__ == '__main__':
    s = [1,2,3]
    print(subsets(s))