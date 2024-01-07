# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 1:
            return TreeNode(nums[0])
        elif len(nums) == 0:
             return None
        else:
            l = nums[:len(nums)//2]
            r = nums[len(nums)//2+1:]
            middleVal = nums[len(nums)//2]
            rightSide = self.sortedArrayToBST(nums[:len(nums)//2])
            leftSide = self.sortedArrayToBST(nums[len(nums)//2+1:])

            return TreeNode(middleVal,rightSide,leftSide)
# driver function
def main():
    # Trie object
    t = Solution()
    print(t.sortedArrayToBST([1,3]))


if __name__ == '__main__':
	main()