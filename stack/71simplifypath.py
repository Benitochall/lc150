def simplifyPath(paths):
    # lets create a stack in python 
    stack = []
    paths = list(paths.split("/"))
    paths =[x for x in paths if x !=  ""]

    for path in paths:
        if path == '..':
            if stack:
                stack.pop()
        elif path == ".":
            continue
        else:
            stack.append(path)

    return "/" +"/".join(stack)
print(simplifyPath("/../"))