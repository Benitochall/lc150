
def generateParenthesis(n):
    answers = []
    # we need open >= closed
    # open and closed >= n

    def backtrack(openCount, closeCount, curr_string):
        if openCount == n and closeCount == n:
            # base case we have found a finished string
            answers.append(curr_string)
        elif openCount == closeCount:
            # the only thing we can do when they are equal
            curr_string = curr_string +'('
            openCount +=1
            backtrack(openCount, closeCount, curr_string)

        elif openCount > closeCount:
            # we can do 2 things 
            old_string = curr_string
            if openCount < n:
                curr_string = curr_string +'('
                c = openCount +1
                backtrack(c, closeCount, curr_string)

            closeCount+=1
            s = old_string +')'
            backtrack(openCount, closeCount, s)
        

    backtrack(0,0,"")
    return answers

generateParenthesis(1)