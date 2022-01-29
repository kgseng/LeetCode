
def missingNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    # 0 to n
    # element = index

    # cyclic sort
    i = 0
    while i < n:
        j = nums[i]
        if nums[i] < n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
        
    # find the element that does not match the index
    for i in range(n):
        if i != nums[i]:
            return i
    return n
    # for num in range(len(nums)+1):
    #     if num not in nums:
    #         return num

nums = [4, 0, 2, 1]
print(missingNumber(nums))