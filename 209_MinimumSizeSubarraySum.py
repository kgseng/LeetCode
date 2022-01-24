def minSubArrayLen(target, nums):
    """
    :type target: int
    :type nums: List[int]
    :rtype: int
    """
    if target > sum(nums):
        return 0
    
    # Left and right pointers, both start at 0
    left = right = 0
    running_sum = 0
    result = 999999
    n = len(nums)
    
    # While the right pointer has not hit the end of the array
    while right < n:
        # Add the right pointer values to running sum
        running_sum += nums[right]
        # If running sum reaches target
        while running_sum >= target:
            # Update our result to minimum of current min win size and prev min win size
            result = min(result, right-left+1)
            # Since we are incrementing the left pointer, subtract the left pointer value from running sum
            running_sum -= nums[left]
            left += 1
        # Increment right pointer
        right += 1
    return result


target = 7
nums = [2,3,1,2,4,3]
# should return 2
print(minSubArrayLen(target, nums))