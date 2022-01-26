# Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n 
# that satisfy the condition nums[i] + nums[j] + nums[k] < target.

def threeSumSmaller(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) < 3: return 0

    # Sort the int array
    nums.sort()

    # res = nums[0] + nums[1] + nums[2]
    count = 0

    for i in range(len(nums)-2):
        j, k = i+1, len(nums) - 1
        while j < k:
            # if less than target, then increment j
            if(nums[i]+nums[j]+nums[k]) < target:
                # *** instead of incrementing by 1, increment by all the numbers between j and k before incrementing j
                count += k-j
                j+=1
            # if greater than or equal to target, decrement k
            else:
                k-=1
    return count 



nums = [-1, 4, 2, 1, 3]
target = 5

print(threeSumSmaller(nums, target))

# Space Complexity
# O(n) for nums.sort() - no in place sorting
# Time Complexity
# num.sort -> n log n
# determining valid triplets -> n^2
# total is n log n + n^2 -> n^2