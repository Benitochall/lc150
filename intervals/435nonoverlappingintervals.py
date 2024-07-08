
def eraseOverlapIntervals(intervals):


    # intuition is to go through the intervals and remove ones that overlap two intervals
    ints = sorted(intervals, key=lambda x: x[0])
    print(ints)
    removed = 0


    # check second index 
    # remove the largest interval if it completly overlaps 
    # remove interval with greater endpoint
    # use a greedy approch, this is because removing the largest interval clears up the back of the array

    if len(intervals) <= 1:
        return 0
    
    i=1

    while i < len(ints):
        start, end = ints[i]

        prev_start, prev_end = ints[i-1]

        # case 1 there is no overlap
        if start >= prev_end:
            i+=1
            continue
        
        #case 2 there is complete overlap
        if start > prev_start and end < prev_end:
            ints.remove([prev_start,prev_end])
            i-=1
            removed +=1

        # case 3 
        else:
            if end > prev_end:
                ints.remove([start, end])
                i-=1
            else:
                ints.remove([prev_start,prev_end])
                i-=1
            removed +=1
        i+=1

    return removed 

print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))