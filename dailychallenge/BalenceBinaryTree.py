def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # construct a new array from a sorted array recursivly, ie take the middle value 
        visited = [] # an array of nodes 
        def inOrderTraversal(node):
            if node.left:
                inOrderTraversal(node.left)
            if node:
                visited.append(TreeNode(node.val))
            if node.right:
                inOrderTraversal(node.right)
        inOrderTraversal(root)


        print(visited[len(visited)//2])

        new_root = visited[len(visited)//2]

        def construct_tree(visited):
            if not visited:
                return None
            
            root = visited[len(visited)//2]

            root.left = construct_tree(visited[:len(visited)//2])
            root.right = construct_tree(visited[len(visited)//2+1:])

            return root

        return construct_tree(visited)