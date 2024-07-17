# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        # first we need to find the nodes to delete
        # just have to dissasociate it with it's parent 
        # maybe do bfs but create a list of modified tree nodes 
        modified_roots = [root]
        queue = [root]

        while queue:
            root = queue.pop(0)
            if root.val in to_delete:
                if root in modified_roots:
                    modified_roots.remove(root)
                if root.left:
                    modified_roots.append(root.left)
                if root.right:
                    modified_roots.append(root.right)

            if root.left:
                queue.append(root.left)
                if root.left.val in to_delete:
                    root.left = None
            if root.right:
                queue.append(root.right)
                if root.right.val in to_delete:
                    root.right = None


        return modified_roots

            
if __name__ == '__main__':
    s = Solution()
    # root = TreeNode(1,TreeNode(2), TreeNode(3, None, TreeNode(4)))
    # root = TreeNode(1,TreeNode(2,TreeNode(4),TreeNode(3)))

    root = TreeNode(1,TreeNode(2,TreeNode(4),TreeNode(5)), TreeNode(3,TreeNode(6),TreeNode(7)))
    delete = [3,5]

    # delete = [2,3]

    # delete = [2,1]
    s.delNodes(root, delete)
            

        