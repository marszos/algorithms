def cal_lps(pat):
    m = len(pat)
    lps = [None] * m 
    lps[0] = 0 
    
    i = 0 
    j = 1 
    
    while j < m:
        if pat[i] == pat[j]:
            i += 1 
            lps[j] = i
            j += 1
        elif i != 0:
            i = lps[i - 1]
        else:
            lps[j] = 0 
            j += 1 
    
    return lps 
    
    
def cal_pmk(pat,s):
    s = s+ s
    m = len(pat)
    n = len(s)
    lps = cal_lps(pat)
    
    i = 0 
    j = 0 
    
    while i < m and j < n:
        if pat[i] == s[j] and i == m - 1:
            return True 
        elif pat[i] == s[j]:
            i += 1 
            j += 1 
        elif i != 0: 
            i = lps[i-1]
        else:
            j += 1 
    
    return False 
    
   
   
s = 'waterbottle'
pat = 'terbottlewa'


cal_pmk(pat,s)
