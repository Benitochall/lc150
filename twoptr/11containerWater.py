def subset_endpoints(array):
    n = len(array)
    endpoints = []
    l= 0
    r= len(array) -1
    max_area = 0

    # Add endpoints for the full array
    while l < r:
        area = (r-l) * min(array[l], array[r])
        max_area = max(area,max_area)

        if array[l] < array[r]:
            l+=1
        else:
            r-=1

    return max_area


   

# Example usage:
array = [1,7,2,5,4,7,3,6]
endpoints = subset_endpoints(array)
print(endpoints)