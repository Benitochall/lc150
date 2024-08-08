from collections import defaultdict
def smolboi(string):

    distict_letters = len(set([x for x in string]))

    i = 0
    j = 0

    d = defaultdict(lambda: 0)
    m = 1000
    count_distinct = 0 

    start_end = (0,0)


    for j in range(len(string)):

        if d[string[j]] == 0:
            d[string[j]] = 1
        else:
             d[string[j]] +=1


        if d[string[j]] ==1:
            count_distinct+=1

        if count_distinct == distict_letters:
            while d[string[i]] > 1:
                if d[string[i]] > 1:
                    d[string[i]] -=1
                    i+=1
                if m > j- i + 1:
                    m = j - i + 1
                    start_end = (i,j)



    return string[start_end[0]:start_end[1]+1]



if __name__ == '__main__':
    i = "aabcbcdbca"
    j = "aaab"
    print(smolboi(i))
    print(smolboi(j))
# Output: dbca