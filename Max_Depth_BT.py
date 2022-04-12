class Node:
    def __init__(self,data) -> None:
        self.data=data 
        self.left=self.right=None
        
root=Node(9)
root.left=Node(10)
root.right=Node(7)
root.right.left=Node(1)
root.right.right=Node(2)
root.right.right.left=Node(4)
root.right.right.right=Node(5)
root.right.right.right.left=Node(6)
root.right.right.right.left.right=Node(60)

def max_depth(root):
    if root is None:
        return 0 
    
    return (1+max(max_depth(root.left), max_depth(root.right)))
