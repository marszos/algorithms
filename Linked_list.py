class node: 
    def __init__(self,data=None):
        self.data = data 
        self.next = None
        

class linkedList:
    
    def __init__(self):
        self.head = node()
        
    
    def append(self,data):
        new_node = node(data)
        cur_node = self.head 
        
        while cur_node.next != None:
            cur_node = cur_node.next 
        cur_node.next = new_node 
        
    def lenght(self):
        cur_node = self.head 
        total = 0 
        
        while cur_node.next != None:
            cur_node = cur_node.next 
            total += 1 
        
        return total 
    
    def display(self):
        elem = []
        cur_node = self.head 
        
        while cur_node.next != None:
            cur_node = cur_node.next 
            elem.append(cur_node.data)
        
        print(elem)
    
    def get(self, index):
        if index >= self.lenght():
            print("ERROR: 'Get' Index out of range")
         
        cur_idx = 0 
        cur_node = self.head 
        
        while True:
            cur_node = cur_node.next
            if index == cur_idx: 
                return cur_node.data
            else:
                cur_idx += 1
     
    
    #delete nth element from linked list
     def erase(self,index):
            cur_node = self.head 
            cur_idx = 0 
        
        while True:
            last_node = cur_node
            cur_node = cur_node.next 
            if cur_idx == index: 
                last_node.next = cur_node.next 
                return 
            else:
                cur_idx += 1 

  lista2 = linkedList()
  lista2.append(1)
  lista2.append(2)
  lista2.append(3)
  
  lista2.display()
  lista2.get(0)
  list1.erase(1)
