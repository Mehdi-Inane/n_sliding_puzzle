from BST import *

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
