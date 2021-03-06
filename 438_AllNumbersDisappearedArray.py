
def findDisappearedNumbers(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    
    i, n = 0, len(nums)
    res = []

    while i < n:
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    
    for i in range(n):
        if i+1 != nums[i]:
            res.append(i+1)
    return res

nums = [4,3,2,7,8,2,3,1]
print(findDisappearedNumbers(nums))