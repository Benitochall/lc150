def sortList(head):
    def merge(list):
        length = len(list)
        if length == 1:
            return list
        left = merge(list[:length//2])
        right = merge(list[length//2:])

        return sort(left,right)

    def sort(head1, head2):
        # return a sorted list
        alen = len(head1)
        blen = len(head2)
        sortedList = []
        ai = 0
        bi=0

        while len(sortedList) != alen +blen:

            if ai < alen and bi < blen:
                if head1[ai] < head2[bi]:
                    sortedList.append(head1[ai])
                    ai+=1
                elif head1[ai] >= head2[bi]:
                    sortedList.append(head2[bi])
                    bi+=1
            elif ai == alen:
                # add the rest of bi
                newList = head2[bi:blen]
                sortedList.extend(newList)
                return sortedList
            else:
                # add the rest of bi
                newList = head1[ai:alen]
                sortedList.extend(newList)
                return sortedList
            
    a =merge(head)
    print(a)
sortList([4,2,1,3])