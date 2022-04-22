def longest_prefix(strs):
    if len(strs) == 0:
        return ("")
    if len(strs) == 1:
        return(strs[0])
    
    pref = strs[0]
    lenp = len(pref)
    
    for s in strs[1:]:
        while pref != s[0:lenp]:
            pref = pref[0:(lenp-1)]
            lenp -= 1 
            
            if lenp == 0:
                return("")
    
    return pref 
  
  
  strs = ["flower","flow","flight"]
  # 'fl'
