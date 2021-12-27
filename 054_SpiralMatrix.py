# Adapted from: https://leetcode.com/problems/spiral-matrix/discuss/999388/95.41-faster-solution
# Explanation:
# 1) Pop out the first item (first row)
# 2) Take what's left
    # a) *matrix -> turn what's inside into arguments for
    # b) zip() -> zips up the given lists of the matrix
    # c) list() -> create list items from given list
    # d) [::-1] -> reverse the order of the list just created
# 3) Repeat until there is no more matrix left to pop from

# Given an m x n matrix, return all elements of the matrix in spiral order.
def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    result = []
    while matrix:
        result += matrix.pop(0)
        matrix = list(zip(*matrix))[::-1]
    return result

test_1 = [[1,2,3],
          [4,5,6],
          [7,8,9]]
          
test_2 = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12]]

test_3 = [[1]]
matrix = test_2
print(spiralOrder(matrix))
