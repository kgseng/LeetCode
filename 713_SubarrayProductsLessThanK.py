def numSubarrayProductLessThanK(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """

    left = 0
    runProd = 1
    count = 0

    for right in range(len(nums)):
        runProd *= nums[right]

        while runProd >= k and left <= right:
            runProd /= nums[left]
            left += 1

        count += (right - left + 1)
    
    return count

nums = [10,5,2,6]
k = 100

print(numSubarrayProductLessThanK(nums,k))


