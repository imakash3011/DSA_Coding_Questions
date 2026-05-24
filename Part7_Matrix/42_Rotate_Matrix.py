def rotate_matrix(matrix):
    print("############### GIVEN MATRIX ###############")
    for row in matrix:
        print(row)
    rows = len(matrix)
    cols =  len(matrix[0])
    # print(rows, cols)
    new_matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    # for rows in new_matrix:
    #     print(rows)
    r,c = 0, len(matrix[0])-1
    for row in range(rows):
        for col in range(cols):
            new_matrix[r][c] = matrix[row][col]   ### First row becomes last column, second row becomes second last column and so on.
            r+=1
        r, c = 0, c-1
    
    print("############### After Rotation - MATRIX ###############")
    for rows in new_matrix:
        print(rows)



matrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
rotate_matrix(matrix)
