def findesmallest(array, val):
    # this is an example of a moving sliding window

    i,j = 0, 1
    min_size = 1000

    while j < len(array):
        s = sum(array[i:j])

        if s <= val:
            j+=1
        elif s > val:
            min_size = min(len(array[i:j]), min_size)
            i+=1

    return min_size
   
        
   

if __name__ == '__main__':
    print(findesmallest([2, 4, 45, 6, 0, 19], 51))
    # should be 3 