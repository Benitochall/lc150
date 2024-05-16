# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # step 1 iterate to the end of both lists
        list_1 = []
        list_2 = []
        while(l1 != None):
            list_1.append(l1.val)
            l1 = l1.next

        while(l2 != None):
            list_2.append(l2.val)
            l2 = l2.next
        
        # need to balance out the array lengths
        max_length = max(len(list_1), len(list_2))
        list_1 += [0] * (max_length - len(list_1))
        list_2 += [0] * (max_length - len(list_2))

        carry = 0
        result = []

        for a,b in zip(list_1, list_2):
            sum = a +b + carry

            carry = sum // 10

            result.append(sum % 10)
        if carry:
            result.append(carry)

        l1 = ListNode(result.pop(0))
        l2 = l1
        for i in range(len(result)):
            l2.next = ListNode(result[i])
            l2 = l2.next

        return l1
        

# chat gpt solution 
def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        dummy = ListNode()
        current = dummy

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0 # check to see if they are null
            val2 = l2.val if l2 else 0
            sum_val = val1 + val2 + carry

            carry = sum_val // 10
            current.next = ListNode(sum_val % 10)

            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
