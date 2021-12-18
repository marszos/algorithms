def isPalindrom(s):
    s = s.replace(' ', '').lower()
    
    count_l = {}
    
    for l in s:
        if l in count_l:
            count_l[l] += 1
        else: 
            count_l[l] = 1
    
    count_odd = 0 
    
    for k,v in count_l.items():
        if v % 2 != 0 and count_odd == 0: 
            count_odd += 1 
        elif v % 2 != 0 and count_odd != 0: 
            return False 
    
    return True 
  
  
  
s1 = 'level'
s2 = 'rotor' 
s3 = 'kayak'
s4 = 'reviver'
s5 = 'This is not a palindrom'

isPalindrom(s5)
