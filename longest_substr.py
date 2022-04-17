def longest_sub(s):
    
    sub = {}
    cur_sub = 0 
    cur_len = 0
    longest = 0
    
    
    for i, letter in enumerate(s):
        if letter in sub and sub[letter] >= cur_sub:
            cur_sub = sub[letter] + 1 
            cur_len = i - sub[letter]
            sub[letter] = i 
        else: 
            sub[letter] = i 
            cur_len += 1 
            if cur_len > longest:
                longest = cur_len
    
    return longest
  
  
  s = 'abcdabbbb'
  
  
  # https://www.youtube.com/watch?v=sUicrnHwA0s
