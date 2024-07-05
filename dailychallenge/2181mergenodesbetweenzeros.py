# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # maybe keep a stack of nodes between zeros
        head = head.next
        prev_list_node = head
        returnNode = None
        foundFirstZero = 0

        summ = 0
        while head:
            if head.val == 0:
                # need to save 

                new_node = ListNode(summ)
                prev_list_node.next = new_node
                summ = 0
                prev_list_node = new_node
                if not foundFirstZero:
                    foundFirstZero = 1
                    returnNode = prev_list_node
            else:
                summ += head.val

            head= head.next

        return returnNode
    
if __name__ == '__main__':
    a = [0,3,1,0,4,5,2,0]
    a =ListNode(0,ListNode(3, ListNode(1, ListNode(0, ListNode(4, ListNode(5, ListNode(2,ListNode(0))))))))
    S = Solution()
    S.mergeNodes(a)