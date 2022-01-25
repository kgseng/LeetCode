def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    left = 1
    for right in range(1, len(nums)):
        # New unique value if not same
        if nums[right] != nums[right-1]:
            # Place unique value at left pointer
            nums[left] = nums[right]
            # Increment left pointer as we have new unique value
            left += 1
    return left


nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))