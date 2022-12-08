from BST import *
from node import * 

class PriorityQueue:
    def __init__(self):
        self.tree= BST()

    def insert(self, node):
        self.tree.insert(node)
        
    def pop(self):
        node_min = minValueNode(self.tree)
        #print("current prio queue")
        self.tree = deleteNode(self.tree,node_min)
        if not self.tree:
            self.tree = BST()
        return node_min

    def isEmpty(self):
        if self.tree.node:
            return False
        return True
    



pt_queue = PriorityQueue()
init_state,goal_state = [[1,2],[3,4]],[[1,2],[3,4]]
node = Node(init_state,goal_state)
node_2 = Node([[1,2],[4,0]],[[1,2],[3,4]])
pt_queue.insert(node)
pt_queue.insert(node_2)
print(pt_queue.tree.left)
pt_queue.pop()
#pt_queue.pop()
tree = pt_queue.tree
print(tree.left)
print(tree.right)
