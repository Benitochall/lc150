def merge(intervals):
       
    combined_intervals = []
    i=0
    intervals.sort(key=lambda x: x[0])

    while (i < len(intervals)):
        if i== 0:
            if intervals[i][1] >= intervals[i+1][0] and intervals[i+1][1] >= intervals[i][1]:
                combined_intervals.append([intervals[i][0], intervals[i+1][1]])
                i+=2
            else:
                combined_intervals.append([intervals[i][0], intervals[i][1]])
                i+=1
        else:
            # pull the last interval
            if len(combined_intervals) > 0:
                last_ele = combined_intervals[-1]
                if last_ele[1] >= intervals[i][0]:
                    last_ele = combined_intervals.pop()
                    a = max(intervals[i][1], last_ele[1])
                    combined_intervals.append([last_ele[0], a])
                    i+=1
                else:
                    combined_intervals.append([intervals[i][0], intervals[i][1]])
                    i+=1
    return combined_intervals


print(merge([[1,4],[2,3]]))