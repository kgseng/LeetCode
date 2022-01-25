def threeSumClosest(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """

    nums.sort()
    res = nums[0] + nums[1] + nums[2]
    for i in range(len(nums) - 2):
        j, k = i+1, len(nums) - 1
        while j < k:
            sum = nums[i] + nums[j] + nums[k]
            if sum == target:
                return sum

            # new sum is found to be closer than stored sum
            if abs(sum-target) < abs(res-target):
                res = sum
            
            # if sum is smaller than target, increment j
            if sum < target:
                j += 1
            elif sum > target:
                k -= 1
    return res
                



nums = [-1,2,1,-4]
target = 1
print(threeSumClosest(nums, target))




