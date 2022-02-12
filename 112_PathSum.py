# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """

        # Go down every path and determine if the running sum == targetSum
        # return True if found, else return False

        def dfs(node, currSum):
            if not node:
                return False
            currSum += node.val
            # no children
            if not node.left and not node.right:
                return currSum == targetSum

            return (dfs(node.left, currSum)) or (dfs(node.right, currSum))
        return dfs(root, 0)
        



