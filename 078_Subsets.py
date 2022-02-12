class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        res = []
        subset = []
        
        def dfs(i):
            if i>= len(nums):
                res.append(subset[:])
                return
            
            # include nums[i]
            subset.append(nums[i])
            dfs(i+1)
            
            # don't include nums[i]
            subset.pop()
            dfs(i+1)
            
        dfs(0)
        return res