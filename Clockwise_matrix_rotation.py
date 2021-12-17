import numpy as np       

def rotation(mat):
    mat = mat[::-1]
    
    for i in range(len(mat)):
        for j in range(i):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    return mat 
  
  
  A = np.array([[1,2,3],[4,5,6],[7,8,9]])
  rotation(A)
