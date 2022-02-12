class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        
        nums = []
        for row in matrix:
            for i in row:
                nums.append(i)
        nums.sort()
        return nums[k-1]