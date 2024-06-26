
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        start = head 
        l = []

        while(head):
            if len(l) < (n+1):
                l.append(head)
            else:
                l.pop(0)
                l.append(head)
            head = head.next

        if len(l) == n:
            return start.next
        elif len(l) == 2:
            l[0].next = None
        else:
            l[0].next = l[2]
        return start
    
if __name__ == '__main__':
    # a = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

    l= ListNode(1,ListNode(2))

    s = Solution()
    s.removeNthFromEnd(l, 2)