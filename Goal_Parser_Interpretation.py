def interpret(command):
    
    ans = ""
    
    for i,ch in enumerate(command):
        if ch == 'G':
            ans += 'G'
        elif ch == '(':
            if command[i+1] == ')':
                ans += 'o'
            else:
                ans += 'al'
    
    return ans 
  
  

# https://leetcode.com/problems/goal-parser-interpretation/
