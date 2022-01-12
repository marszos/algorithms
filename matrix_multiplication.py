def matmul(m1,m2):
    r = []
    m = []
    
    
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            sums = 0 
            for k in range(len(m2)):
                sums = sums + (m1[i][k] * m2[k][j])
            
            r.append(sums)
        m.append(r)
        r = []
    return m 
  
  
  ##### one-liner 
  
  def matmul(m1,m2):
    
    return [ [sum(x * y for x,y in zip(m1_row, m2_col)) for m2_col in zip(*m2)] for m1_row in m1
        
    ]
  
  
m1 = [[1, 2, 3], [4, 5, 6]]
m2 = [[7, 8], [9, 10], [11, 12]]
