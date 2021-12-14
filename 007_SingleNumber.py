class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # any number XOR itself = 0
        # XOR everything and you'll be left with 0 XOR (single element) = single element
        for i in range(1, len(nums)):
            nums[0] ^= nums[i]
        return nums[0]
