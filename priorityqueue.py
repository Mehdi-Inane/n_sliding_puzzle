import heapq
from typing import Union
from BST import *

class PriorityQueue:
    """A priority queue implementation based on heapq"""
    def __init__(self) -> None:
        """Initialize the priority queue to an empty list"""
        self.tree= Node()
    def isEmpty():
    	if self.tree:
    		return True
    	else:
    		return False
        
    def insert(self, node) -> None:
        """Add an item to the priority queue"""
        self.tree.insert(node)
        
    def pop():
    	node_min = minValueNode(self.tree)
    	self.tree = deleteNode(self.tree,node_min)
    	return node_min
