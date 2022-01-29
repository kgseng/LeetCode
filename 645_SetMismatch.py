def findErrorNums(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """

    # 1) Cyclic Sort, [1,n]
    # 2) Find the mismatch and return the element, index of mismatch

    res = []
    i, n = 0 , len(nums)

    while i < n:
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    
    for i in range(n):
        if nums[i] != i + 1:
            return [nums[i], i+1]
    return res




nums = [1,2,2,4]
# [2,3]
print(findErrorNums(nums))