def maxProduct(nums):
    # Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.
    """
    :type nums: List[int]
    :rtype: int
    """
    # Kedane's Algorithm; with each iteration, track min and max since the min can become new max. 

    # Set variables to track previous iteration's min and max, alongside a global max we are returning.
    prevMin = prevMax = globalMax = nums[0]

    # Starting with second number, for each number in array
    for num in nums[1:]:
        # <Current run's> minimum product is the minimum of [current number, current number * running max, current number * running min]
        # <Current run's> maximum product is the maximum of [current number, current number * running max, current number * running min]
        minProd = min(num, prevMax*num, prevMin*num)
        maxProd = max(num, prevMax*num, prevMin*num)

        # Store these values before running next iteration for comparison's sake
        prevMin = minProd
        prevMax = maxProd

        # During each iteration, the maxProd calculated is compared against our globalMax
        globalMax = max(globalMax, maxProd)
    
    return globalMax

nums = [-2,3,-4]
print(maxProduct(nums))