
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        #idea create a dictionary of node val and position
        # 
        node_map = {}
        curr = head
        # create a mapping of curr to new node
        while curr:
            node_map[curr] = Node(curr.val)
            curr = curr.next
        
        # Update the next and random pointers for the copies
        curr = head
        while curr:
            if curr.next:
                node_map[curr].next = node_map[curr.next]
            if curr.random:
                node_map[curr].random = node_map[curr.random]
            curr = curr.next
        
        return node_map[head]

if __name__ =='__main__':
    S = Solution()

    # n1 = Node(7)
    # n2 = Node(13)
    # n3 = Node(11)
    # n4 = Node(10)
    # n5 = Node(1)

    # n1.next = n2
    # n1.random = None
    # n2.next = n3
    # n2.random = n1
    # n3.next = n4
    # n3.random = n5
    # n4.next = n5
    # n4.random = n3
    # n5.next = None
    # n5.random = n1

    # Creating the sample linked list with random pointers
    n1 = Node(3)
    n2 = Node(3)
    n3 = Node(3)

    # Linking the nodes as per the input: [[3,null],[3,0],[3,null]]
    n1.next = None
    n1.random = None

    n2.next = n3
    n2.random = n1

    n3.next = None
    n3.random = None


    copied_head = S.copyRandomList(n1)