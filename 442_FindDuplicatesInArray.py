def findDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    # 1) Cyclic Sort nums in place
    # 2) Iterate through nums appending elements that do not match their index (i+1) for [1,n]

    i, n = 0, len(nums)
    res = []

    while i < n:
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    
    for i in range(n):
        if nums[i] != i+1:
            res.append(nums[i])
    res.sort()
    return res
    

nums = [4,3,2,7,8,2,3,1]
# [2,3]
print(findDuplicates(nums))