# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reorderList(self, head):
        if not head or not head.next:
            return
        
        # This is how I find the middle of the list
        # we keep a slow pointer and a fast pointer 
        # the slow pointer goes half as fast as the fast pointer so 
        # when there is no longer a fast we have reaached the middle of the list 

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        
        
        # `slow` is now at the middle of the linked list
        middle = slow
        #now we need to reverse the second half of the liked list becasue that way we can alternate 
        # when we merge them together

        prev, curr = None, middle
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
           
        
        # `prev` is now the head of the reversed second half
        # Step 3: Merge the first half and the reversed second half
        first_half, second_half = head, prev
        while second_half.next:


            temp = first_half.next
            # make the next value of the first half the first of the second
            first_half.next = second_half
            # move the fist half up one 
            first_half = temp
            
            temp = second_half.next
            # make the second_halfs pointer the first one 
            second_half.next = first_half
            #move the second half up one
            second_half = temp

    
if __name__ == '__main__':
    a = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

    s = Solution()
    s.reorderList(a)