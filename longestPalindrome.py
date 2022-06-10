def longestPalindrome2(s):
    char_count = {}
    
    for ch in s:
        char_count[ch] = char_count.get(ch,0) + 1 
        
    final_count = 0 
    odd_is_present = False 
    
    for k in char_count:
        if char_count[k] % 2 == 0:
            final_count += char_count[k]
        else:
            final_count += (char_count[k] - 1)
            odd_is_present = True 
    
    if odd_is_present == True:
        final_count += 1 
    
    
    return final_count
  
  # https://leetcode.com/problems/longest-palindrome/submissions/
