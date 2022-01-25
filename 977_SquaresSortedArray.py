# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

def sortedSquares(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """

    res = []
    for num in nums:
        res.append(num**2)
    res.sort()
    return res

nums = [-4,-1,0,3,10]
print(sortedSquares(nums))