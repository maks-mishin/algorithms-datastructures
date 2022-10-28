def rotate_one_step(matrix: list, rows: int, cols: int) -> None:
    """Rotates the matrix one step clockwise"""
    top, bottom = 0, rows - 1
    left, right = 0, cols - 1

    # we calculate count of rotated layers and then rotate each layer
    count_layers_rotated = int(rows / 2)
    for _ in range(count_layers_rotated):
        top_left = matrix[left][left]
        
        for i in range(top, bottom):
            matrix[i][left] = matrix[i + 1][left]
        
        for j in range(left, right):
            matrix[bottom][j] = matrix[bottom][j + 1]
        
        for i in range(bottom - 1, top - 1, -1):
            matrix[i + 1][right] = matrix[i][right]
            
        for j in range(right - 1, left, -1):
            matrix[top][j + 1] = matrix[top][j]
        
        matrix[left][left + 1] = top_left
        
        if left == cols - 1 or top == rows - 1:
            break
        top, bottom = top + 1, bottom - 1
        left, right = left + 1, right - 1


def MatrixTurn(matrix: list, rows: int, cols: int, steps: int) -> None:
    """Rotates the matrix by the number of steps 'steps'"""

    # convert each row to list because of
    # 'str' object does not support item assignment
    for i, row in enumerate(matrix):
        matrix[i] = list(row)
    
    for _ in range(steps):
        rotate_one_step(matrix, rows, cols)
    
    # convert back to str
    for i, row in enumerate(matrix):
        matrix[i] = ''.join(row)
