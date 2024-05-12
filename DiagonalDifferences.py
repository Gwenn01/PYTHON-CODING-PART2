def diagonalDifferences(matrix):
    # left 1 5 9 = 15 right 3 5 9 = 17 then 15 - 17 = 2
    left_diagonal = 0
    right_diagonal = 0
    row = len(matrix)-1
    j = row
    for i in range(row):
        left_diagonal += matrix[i][i]
        right_diagonal += matrix[i][j]
        j -= 1
      
    differences = left_diagonal - right_diagonal
    return abs(differences)
    
    
matrix = [
[1, 2, 3],
[4, 5, 6], 
[9, 8, 9]
]
print(diagonalDifferences(matrix))