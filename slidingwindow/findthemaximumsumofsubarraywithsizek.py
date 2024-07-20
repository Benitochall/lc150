def findmax(array, k):
    # this is an example of a fixed sliding window
    m = -100
    for i in range(0, len(array)-k+1):
        s = sum(array[i:k+i])
        m = max(s,m)
        
    print(m)

if __name__ == '__main__':
    findmax([1, 4, 2, 10, 2, 3, 1, 0, 20], 4)