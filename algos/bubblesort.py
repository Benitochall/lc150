# the idea behind bubble sort is to bubble the smallest elements to the top of the list
# this is o(n^2)

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr)-1-i):
            # need to swap i, j
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubble_sort([5,4,3,2,1]))