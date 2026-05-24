def spiral_print(matrix):
    if not matrix:
        return

    print("########### SPIRAL ORDER ###########")
    
    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1
    
    while top <= bottom and left <= right:
        # 1. Print Top Row (Left to Right)
        for i in range(left, right + 1):
            print(matrix[top][i], end=" ")
        top += 1

        # 2. Print Right Column (Top to Bottom)
        for i in range(top, bottom + 1):
            print(matrix[i][right], end=" ")
        right -= 1

        # 3. Print Bottom Row (Right to Left)
        if top <= bottom: # Check to ensure we haven't crossed paths
            for i in range(right, left - 1, -1):
                print(matrix[bottom][i], end=" ")
            bottom -= 1

        # 4. Print Left Column (Bottom to Top)
        if left <= right: # Check to ensure we haven't crossed paths
            for i in range(bottom, top - 1, -1):
                print(matrix[i][left], end=" ")
            left += 1
    print() # New line at the end

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
spiral_print(matrix)