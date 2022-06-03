class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.history = [homepage]
        self.curr_idx = 0

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        self.curr_idx += 1 
        self.history = self.history[0:self.curr_idx]
        self.history.append(url)
        
        

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        self.curr_idx = max(0, self.curr_idx - steps)
        return self.history[self.curr_idx]
       
        

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        self.curr_idx = min(len(self.history) -1, self.curr_idx+steps)
        return self.history[self.curr_idx]
      
      
      
   # https://leetcode.com/problems/design-browser-history/
        
