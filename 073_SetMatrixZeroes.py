# Helper Functions
# Zeroes out every index of the given row
def zeroOutRow(self, row):
    """
    :type row: List[int]
    :rtype: None; modify the given row
    """
    for i in range(len(row)):
        row[i] = 0
# Zeroes out the specified col of the given matrix
def zeroOutCol(self, matrix, col):
    """
    :type matrix: List[List[int]], 
             col: int
    :rtype: None, modify the specified col of each matrix[row]
    """
    for row in matrix:
        row[col] = 0

# Main Function
# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.    
def setZeroes(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """

    # Initial Thoughts
        # Parse through matrix and store row/col zeroes
        # Check if row/col has been stored before to prevent revisits
        # Zero out each stored row/col

    rowList = []
    colList = []
    i,j= 0,0

    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[i])):
            if matrix[i][j] == 0:
                if i not in rowList:
                    rowList.append(i)
                if j not in colList:
                    colList.append(j)
    for num in rowList:
        self.zeroOutRow(matrix[num])
    for num in colList:
        self.zeroOutCol(matrix, num)

# Test Casees
# case_1 = [[1,1,1],[1,0,1],[1,1,1]
# case_2: [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# case_3: [[0], [1]]
# matrix = case_1
# print(setZeroes(matrix))