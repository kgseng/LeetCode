def findDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    i, n = 0, len(nums)
    while i < n:
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    
    # now we iterate through nums and find which position does not match, as there is only (1) duplicate
    for i in range(n):
        if i+1 != nums[i]:
            return nums[i]
    return n
    


nums = [1,3,4,2,2]
print(findDuplicate(nums))