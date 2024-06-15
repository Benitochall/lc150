
def insert2(intervals, newInterval):
    """
    :type intervals: List[List[int]]
    :type newInterval: List[int]
    :rtype: List[List[int]]
    """
    # first thing is find the lowest interval right side of interval that overlaps
    if not intervals:
        return newInterval
    newInterval_l = newInterval[0]
    newInterval_h = newInterval[1]

    foundLow = -2
    foundHigh = -2

    for i, inv in enumerate(intervals):
        inv_l = intervals[len(intervals)-1-i][0]
        inv_h = inv[1]

        if inv_h >= newInterval_l and foundLow== -2:
            foundLow = i
        if inv_l <= newInterval_h and foundHigh == -2:
            foundHigh = len(intervals) -i -1

        if foundHigh != -2 and foundLow != -2:
            break

    # take the min of the inv_l and
    new_intervals = []

    if foundHigh != -2 and foundLow != -2:
        new_intervals.append([min(intervals[foundLow][0], newInterval_l), intervals[foundLow][1]])
        new_intervals.append([intervals[foundHigh][0], max(intervals[foundHigh][1], newInterval_h)])
        new_intervals = intervals[:foundLow] + [[new_intervals[0][0], new_intervals[1][1]]] + intervals[foundHigh+1:]
    elif foundLow == -2:
        new_intervals = intervals+ [newInterval]
    elif foundHigh == -2:
        new_intervals = [newInterval] + intervals
    return new_intervals
                
def insert(intervals, newInterval):

    if not intervals:
        return [newInterval]
    start= newInterval[0]
    end = newInterval[1]

    new_list = []

    if end < intervals[0][0]:
        return [newInterval] + intervals
    if start > intervals[len(intervals)-1][1]:
        return intervals + [newInterval]



    while intervals:
        i,j = intervals.pop(0)

        if i <= start <= j:
            start, end = [min(i,start),max(j,end)]

        elif i <= end <= j:
            new_list.append([min(i,start),max(j,end)])
        elif start < i and end > j:
            continue
        else:
            new_list.append([i,j])

    return new_list

           



       

print(insert([[2,2.5],[3,5],[6,7],[8,10],[12,16]], [0,1]))