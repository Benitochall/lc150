def merge(ar1, ar2):
    i, j = 0, 0
    mergedArray = []
    while i < len(ar1) and j < len(ar2):
        if ar1[i] < ar2[j]:
            mergedArray.append(ar1[i])
            i += 1
        else:
            mergedArray.append(ar2[j])
            j += 1
    while i < len(ar1):
        mergedArray.append(ar1[i])
        i += 1
    while j < len(ar2):
        mergedArray.append(ar2[j])
        j += 1

    return mergedArray
        
    
def mergeSort(array):
    if len(array) ==1:
        return array
    else:
        middle = len(array)//2
        rightSide= mergeSort(array[middle:])
        leftSide = mergeSort(array[:middle])

    return(merge(leftSide,rightSide))

print(mergeSort([89, 24, 56, 11, 72, 33, 49, 7, 94, 18, 61, 42]))

#print(mergeSort([89, 24, 56, 11]))
