from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    @staticmethod
    def rightSideView(root):
        if not root:
            return []

        result = []
        queue = deque([root]) # queue is intiallized with the root node
        print(queue)

        while queue:
            level_size = len(queue) # this is the current 

            rightmost_node = None # 
            for i in range(level_size): # this is the current amount of nodes on the level 
                current_node = queue.popleft() # for each node in the level I get the left node of the queue
                # we keep going through the left nodes 

                rightmost_node = current_node.val # set the current node as the right most node

                if current_node.left: # if the current node has a left append the left 
                    queue.append(current_node.left) 
                if current_node.right: # if the current node is the right append the right to the queue 
                    queue.append(current_node.right)

            result.append(rightmost_node) # this will only add the queue on the left

        return result

    @staticmethod
    def main():
        print("main")
        node4 = TreeNode(4)
        node3 = TreeNode(3)
        node2 = TreeNode(2, left=node4)
        node1 = TreeNode(1, left=node2, right=node3)
        solution = Solution()
        print(solution.rightSideView(node1))

if __name__ == "__main__":
    Solution.main()
