# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: 
            return 0
        queue = deque([(root, 1)])
        level = 0
        
        while queue:
            node, level = queue.popleft()
            if node is None:
                continue
            if not node.left and not node.right: 
                return level
            queue.append((node.left, level+1))
            queue.append((node.right, level+1))
