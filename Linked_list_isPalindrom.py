class node:
    def __init__(self, data, next = None):
        self.data = data 
        self.next = next 


def linked_list(elements):
    head = node(elements[0])
    
    for element in elements[1:]:
        ptr = head
        
        while ptr.next:
            ptr = ptr.next 
        ptr.next = node(element)
        
    return head 
  
  
  head = linked_list([1,2,3,2,1])
  
  class Solution:
    def isPalindrom(self, head):
        slow = head 
        fast = head 
        stack = []
        
        while fast and fast.next:
            stack.append(slow.data)
            fast = fast.next.next 
            slow = slow.next 
        if fast:
            slow = slow.next 
        
        
        while stack and slow:
            if slow.data != stack.pop():
                return False 
            else:
                slow = slow.next 
        
        return True 
