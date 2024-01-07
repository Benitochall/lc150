def isValid(s):
        # lets create a stack in python 
    stack = []
    for letter in s:
        if letter in ['(', '{', '[']: 
            # these are opening brackets need to push to stack
            stack.append(letter)
        else:
            if stack:
                a = stack.pop()
                if a == '(' and letter != ')':
                    return False
                elif a == '{' and letter != '}':
                    return False
                elif a == '[' and letter != ']':
                    return False
            else:
                return False
    if not stack:
        return True 
    return False
print(isValid("(){}}{"))

        
        