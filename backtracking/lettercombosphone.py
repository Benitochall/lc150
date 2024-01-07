#this file uses backtrackting as means of solving this problem
def letterCombinations(digits):

    def backtrack(index, path):
        # If the path is of the same length as digits, add it to the result
        if index == len(digits):
            result.append(''.join(path))
            return

        current_digit = int(digits[index]) #get the current digit 
        letters = num_dict[current_digit]

        # Iterate through each letter and recursively call the backtrack function
        for letter in letters:
            path.append(letter)
            backtrack(index + 1, path)
            path.pop()

    if not digits:
        return []

    num_dict = {
        2: ['a', 'b', 'c'],
        3: ['d', 'e', 'f'],
        4: ['g', 'h', 'i'],
        5: ['j', 'k', 'l'],
        6: ['m', 'n', 'o'],
        7: ['p', 'q', 'r', 's'],
        8: ['t', 'u', 'v'],
        9: ['w', 'x', 'y', 'z']
    }

    result = []
    backtrack(0, [])
    return result
print(letterCombinations("234"))
