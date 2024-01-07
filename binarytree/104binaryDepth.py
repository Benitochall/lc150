class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxDepth(self, root):
        if root is None:
            return 0
        else:
            lDepth = self.maxDepth(root.left)
            rDepth = self.maxDepth(root.right)
            if lDepth > rDepth:
                return lDepth + 1
            else:
                return rDepth + 1

    @staticmethod
    def main():
        print("main")
        node2 = TreeNode(2)
        node4 = TreeNode(4)
        node5 = TreeNode(5)
        node3 = TreeNode(3, node4 ,node5)
        node1 = TreeNode(1, node2, node3)
        solution = Solution() # creates an instance of solution
        print(solution.maxDepth(node1))

if __name__ == "__main__":
    Solution.main()
