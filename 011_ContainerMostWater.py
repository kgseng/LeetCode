# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.

def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    # need to store the running maxArea and compare it against a globalMax
    # when using two integers, area is calculated using the lower height[i]
    # area = length * width
    # area = (lower of the two indices) * (difference between indices)

    a, b = 0, len(height) - 1
    area = 0

    while a < b:
        area = max(area, min(height[a], height[b]) * abs(a-b))
        if height[a] < height[b]:
            a += 1
        else:
            b -= 1
    return area

height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))
