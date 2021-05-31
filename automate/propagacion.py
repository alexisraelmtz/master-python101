
matrix = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 0], # 
    [0, 1, 0, 0, 0, 0, 1, 1],
    [0, 0, 1, 0, 2, 0, 0, 0],
    [0, 0, 1, 0, 2, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
]

# DFS
def fill(matrix, x, y, fill_val):
    size = len(matrix)
    # visited = [False for _ in range(size) for _ in range(len(matrix[0]))]
    def helper(matrix, x, y, fill_val)
        initVal = matrix[x][y]
        matrix[x][y] = fill_val
        
        if x != 0:
            x1 = matrix[x-1][y]
            if initVal == x1:
                # matrix[x][y] = fill_val
                return helper(matrix, x-1, y, fill_val)
                
        if y != 0:
            x1 = matrix[x][y-1]
            if initVal == x1:
                # matrix[x][y] = fill_val
                return helper(matrix, x-1, y, fill_val)
                

        # pos 0

    return matrix 
                
     