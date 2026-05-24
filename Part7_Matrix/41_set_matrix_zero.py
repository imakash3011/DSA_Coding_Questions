def set_zero(matrix):
    row_lst = set() # Using a set is faster and prevents duplicates automatically
    col_lst = set()
    rows = len(matrix)
    cols = len(matrix[0])

    # 1. Identify which rows and columns should be zeroed
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                row_lst.add(i)
                col_lst.add(j)

    # 2. Zero out the identified rows
    for r in row_lst:
        for c in range(cols):
            matrix[r][c] = 0

    # 3. Zero out the identified columns
    for c in col_lst:
        for r in range(rows):
            matrix[r][c] = 0

    # Visualizing the output
    for row in matrix:
        print(row)

matrix = [[7,9,2,3], [20,8,0,10], [29,0,-10,5], [4,14,6,7]]
set_zero(matrix)