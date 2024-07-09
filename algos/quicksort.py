import random
def quicksort(list, low, high):
    def partition(arr, low, high):

        rand_i = random.randint(low, high)

        # swap with high value
        arr[rand_i], arr[high] = arr[high], arr[rand_i]

        pivot = arr[high]

        i = low -1 # keeps track of the lower values than the pivot

        for j in range(low, high):
            if arr[j] <= pivot:
                i = i+1

                #swap j and the i 
                arr[i], arr[j] = arr[j], arr[i]

        # swap the pivot and the closest value lower than it
        arr[i + 1], arr[high] = arr[high], arr[i + 1]


        return i+1 # the current position of the pivot

    if low < high:
        partition_i = partition(list, low, high)

        #recurse on left
        quicksort(list, low, partition_i-1)

        #recurse on right 
        quicksort(list, partition_i +1, high)
    return list



l = [8,7,6,5,4,3,2,1]
print(quicksort(l, 0, len(l)-1))