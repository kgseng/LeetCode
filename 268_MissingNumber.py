class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        for num in range(len(nums)+1):
            if num not in nums:
                return num
            