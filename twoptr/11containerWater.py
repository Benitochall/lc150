def subset_endpoints(array):
    n = len(array)
    endpoints = []

    # Add endpoints for the full array
    endpoints.append((array[0], array[-1]))

    # Iterate over different subset sizes
    for size in range(n - 1, 1, -1):  # Start from n-1 down to 1
        for i in range(n - size + 1):
            endpoints.append((array[i], array[i + size - 1]))

    return endpoints

# Example usage:
array = [1, 4, 2, 6, 7]
endpoints = subset_endpoints(array)
print(endpoints)