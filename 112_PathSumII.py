# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(root, targetSum, [], res)
        return res
    
    def dfs(self, node, currSum, currPath, res):
        if not node:
            return
        currPath.append(node.val)
        if currSum == node.val and not node.left and not node.right:
            res.append(list(currPath))
        else:
            self.dfs(node.left, currSum-node.val, currPath, res)
            self.dfs(node.right, currSum-node.val, currPath, res)
        del currPath[-1]
        