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
        if self.tree:
            return False
        return True
    



"""pt_queue = PriorityQueue()
init_state,goal_state = [[2,1],[3,0]],[[1,2],[3,0]]
node = Node(init_state,goal_state)
print(node.n)
pt_queue.insert(node)
node_list = node.expand()
for nod in node_list:
    pt_queue.insert(nod)
print(pt_queue.tree.left)
print("treeval",pt_queue.tree.value)
print(pt_queue.pop().n)
print(minValueNode(pt_queue.tree).n)

print(node.n)
#pt_queue.pop()
tree = pt_queue.tree
print(tree)
pt_queue.pop()
print(tree.left)"""
