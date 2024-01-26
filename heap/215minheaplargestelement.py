class TreeNode(object):
    def __init__(self, val=0, left=None, right=None,parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

class Heap(object):
    def __init__(self):
        self.size = 0
        self.root = None

    def insert(self, val):
        new_node = TreeNode(val)

        if self.size == 0:
            self.root = new_node
            self.size +=1
            return


        parent = (self.size - 1) // 2
        self.size +=1
        parent_node = self.get_node_at(parent)

        if parent_node.left is None:
            parent_node.left = new_node
        else:
            parent_node.right = new_node
        new_node.parent = parent_node

        # Heapify by moving the new node up to its correct position
        self.heapify_up(new_node)
    def pop(self):
        # returns the largest element and then percolates down 
        largest_val = self.root
        # need to get the left most value in the tree
        left_most = (self.size-1)
        left_most_node = self.get_node_at(left_most) # need to check this 

        # configure the left_most_node as the current root
        #update parenent refrences of ola
        if largest_val.left:
            largest_val.left.parent = left_most_node
            left_most_node.left = largest_val.left
        if largest_val.right:
            largest_val.right.parent = left_most_node
            left_most_node.right = largest_val.right
        
        if left_most_node.parent and left_most_node.parent.left == left_most_node:
            left_most_node.parent.left = None
        if left_most_node.parent and left_most_node.parent.right == left_most_node:
            left_most_node.parent.right = None
        
        left_most_node.parent = None
        self.root = left_most_node

        self.percolate_down(left_most_node)
        self.size -=1
        return largest_val.val

    def percolate_down(self, node):
        # restructures the heap after deleteing one node 
        # take the smallest value in the heap 
        while node.left and node.right and (node.val > node.right.val or node.val > node.left.val):
            # find the largest of the two nodes 
            if node.right.val < node.left.val:
                largestNode = node.right
            else:
                largestNode = node.left
            
            largestNodeRight = largestNode.right
            largestNodeLeft = largestNode.left

            if largestNode == node.right:
                largestNode.left = node.left
                largestNode.right = node
                largestNode.parent = node.parent
                #update parents 
                if node.left:
                    node.left.parent = largestNode
                if node.parent and node == node.parent.left:
                    node.parent.left = largestNode
                elif node.parent and node == node.parent.right:
                    node.parent.right = largestNode
                
                node.parent = largestNode
                node.left = largestNodeLeft
                node.right = largestNodeRight

                # change parent of subsidary nodes 
                if largestNodeRight:
                    largestNodeRight.parent = node
                if largestNodeLeft:
                    largestNodeLeft.parent = node

                
            elif largestNode == node.left:
                largestNode.left = node
                largestNode.right = node.right
                largestNode.parent = node.parent
                #update parents 
                if node.right:
                    node.right.parent = largestNode
                if node.parent and node == node.parent.left:
                    node.parent.left = largestNode
                elif node.parent and node == node.parent.right:
                    node.parent.right = largestNode
                
                node.parent = largestNode
                node.left = largestNodeLeft
                node.right = largestNodeRight

                # change parent of subsidary nodes 
                if largestNodeRight:
                    largestNodeRight.parent = node
                if largestNodeLeft:
                    largestNodeLeft.parent = node
            if node == self.root:
                self.root = largestNode

    def heapify_up(self, node):
        while node.parent is not None and node.val < node.parent.val:
            currNode = node
            parNode = node.parent
            # grandParNode = parNode.parent
            # # check to see if parent is root 
            if self.root == parNode:
                self.root = node
            
            # take care of P-> currNode
            if parNode.parent and parNode.parent.left == parNode:
                parNode.parent.left = currNode
            elif parNode.parent and parNode.parent.right == parNode:
                parNode.parent.right = currNode

            
            
            if parNode.left == currNode:
                # this is the case of a left node 
                tempCurrNodeLeft = currNode.left
                tempCurrNodeRight = currNode.right


                currNode.right = parNode.right
                currNode.left = parNode
                if parNode.right:
                    parNode.right.parent = currNode #specific to left 
                currNode.parent = parNode.parent

                # take care of new node 
                parNode.left = tempCurrNodeLeft
                parNode.right = tempCurrNodeRight
                parNode.parent = currNode
            elif parNode.right == currNode: 
                # this is a right node
                tempCurrNodeLeft = currNode.left
                tempCurrNodeRight = currNode.right


                currNode.left = parNode.left
                currNode.right = parNode
                if parNode.left:
                    parNode.left.parent = currNode #specific to left 
                currNode.parent = parNode.parent

                # take care of new node 
                parNode.left = tempCurrNodeLeft
                parNode.right = tempCurrNodeRight
                parNode.parent = currNode



    def get_node_at(self, index):
        binary_str = bin(index + 1)[3:]
        node = self.root
        for char in binary_str:
            if char == '0':
                node = node.left
            else:
                node = node.right
        return node

def findKthLargest(nums, k):
    a = Heap()
    for number in nums:
        if a.size < k:
            a.insert(number)
        elif number > a.root.val:
            a.pop()
            a.insert(number)
    
    print(a.pop())
    
def main():
    array = [3,2,1,5,6,4]
    k = 2
    findKthLargest(array, k)
   

if __name__ == "__main__":
    main()
