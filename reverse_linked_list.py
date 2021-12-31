class node:
    def __init__(self, data = None):
        self.data = data 
        self.next = None 

class linlist:
    def __init__(self):
        self.head = None 
    
    def push(self, data):
        new_node = node10(data)
        new_node.next = self.head 
        self.head = new_node
        
    def display(self):
        temp = self.head 
        
        while (temp):
            print(temp.data)
            temp = temp.next 
            
            
    def reverse(self):
        prev = None 
        curr = self.head 
        
        while curr != None:
            next = curr.next 
            curr.next = prev
            prev = curr
            curr = next 
        self.head = prev
