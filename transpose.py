def transpose(mat):
    result = result = [[0 for i in range(len(mat))] for j in range(len(mat[0]))]
    
    for i in range(len(mat[0])):
        for j in range(len(mat)):
            result[i][j] = mat[j][i]
            
    return result
