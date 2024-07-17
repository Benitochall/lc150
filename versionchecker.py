def version_compare(version1, version2):
    # need to check version 1 compared to version 2
    a = version1.split(".")
    b = version2.split(".")

    if len(a) <= len(b):
        for i in range(len(a)):
            if a[i] < b[i]:
                return -1
            elif a[i] > b[i]:
                return 1
        if len(a) < len(b):
            for j in range(len(a), len(b)):
                if b[j] != "0" :
                    return -1
                elif j == len(b)-1:
                    return 0
    
    if len(b) <=len(a):
        for i in range(len(b)):
            if b[i] < a[i]:
                return -1
            elif b[i] > a[i]:
                return 1
        # there still could be b's left over
        if len(b) < len(a):
            for j in range(len(b), len(a)):
                if a[j] != "0" :
                    return -1
                elif j == len(a)-1:
                    return 0 
            
    return 0

print(version_compare("2.10.0.1", "2.1.0.10"))