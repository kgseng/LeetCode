# Problem Statement 
# We are given an array containing ‘n’ objects. Each object, when created, was assigned a unique number from 1 to ‘n’ based on their creation sequence. 
# This means that the object with sequence number ‘3’ was created just before the object with sequence number ‘4’.
# Write a function to sort the objects in-place on their creation sequence number in O(n) and without any extra space. 
# For simplicity, let’s assume we are passed an integer array containing only the sequence numbers, though each number is actually an object.


def cyclic_sort(nums):
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]  # swap
        else:
            i += 1
    return nums


input = [3, 1, 5, 4, 2]
output = [1,2,3,4,5]
print(cyclic_sort(input)==output)
