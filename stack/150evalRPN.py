
def evalRPN(tokens):
    """
    :type tokens: List[str]
    :rtype: int
    """
    # push it on the stack and then pull it back off
    res = 'a'
    stack = []
    for item in tokens:
        if item not in ['+', '-', '/', '*']:
            stack.append(item)
        else:
            # pull off the stack
            if res == 'a':
                divisor = int(stack.pop())
                dividend = int(stack.pop())
                if item == '+':
                    res = dividend + divisor
                elif item == '-':
                    res = dividend - divisor
                elif item == '*':
                    res = dividend * divisor
                else:
                    res = dividend // divisor
            else:
                partial = int(stack.pop())
                if item == '+':
                    res = res + partial
                elif item == '-':
                    res = partial - res
                elif item == '*':
                    res = res * partial
                else:
                    if abs(partial) < abs(res):
                        res = 0
                    else:
                        res = partial // res

evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])