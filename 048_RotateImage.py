def rotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """

    # Rotate the image in place
    # Invert rows, invert along y=-x

    # Start: matrix = [[1,2,3],
    #                  [4,5,6],
    #                  [7,8,9]]

    # Step 1: Reverse matrix
    # Since matrix is [], can reverse matrix via [::-1] or .reverse()
    #        matrix = [[7,8,9],
    #                  [4,5,6],
    #                  [1,2,3,]]

    # Step 2: Invert matrix along diagonal
    # For i, j ; matrix[i,j] becomes matrix[j,i] and matrix[j,i] becomes matrix[i,j]
    # where i is len(matrix)  (0...1....2..)
    # where j is i            (0...1....2)
    #   (0,0), (0,1), (0,2), (1, 1), (1,2), (2,2)
    # if we don't restrict j to i, we do a double swap and the matrix appears unchanged
    
    # Result:
    #        matrix = [[7,4,1],
    #                  [8,5,2],
    #                  [9,6,3,]]
    # Looks as if the matrix has been rotated 90 degrees

    matrix.reverse()
    i, j, = 0, 0
    for i in range(len(matrix)):
        for j in range(i):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
    return matrix

matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
print(rotate(matrix))