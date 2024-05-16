def fill_zeros(array1, array2):
    sum1 = sum(array1)
    sum2 = sum(array2)

    diff = abs(sum1 - sum2)


    if sum1 > sum2:
        array = array2
    else:
        array = array1

    zeros_to_fill = min(array1.count(0), array2.count(0))

    if diff == 0 and array1.count(0) == array2.count(0):
        return -1

    for i in range(len(array1)):
        if array1[i] == 0 and zeros_to_fill > 0:
            array1[i] = diff // zeros_to_fill
            diff -= array1[i]
            zeros_to_fill -= 1
    
    for i in range(len(array2)):
        if array2[i] == 0:
            array2[i] = diff // zeros_to_fill
            diff -= array2[i]
            zeros_to_fill -= 1

    return array1, array2

# Example arrays
array1 = [1, 2, 0]
array2 = [1, 3, 0, 0]

filled_array1, filled_array2 = fill_zeros(array1, array2)
print("Filled Array 1:", filled_array1)
print("Filled Array 2:", filled_array2)
