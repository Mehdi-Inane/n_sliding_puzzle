
import queue
from node import *
from puzzle import *
from BST import * 
import sys
sys.setrecursionlimit(1000000)
class BiSearch:


    def __init__(self,init_state,goal_state,heuristic):
        self.src_queue = queue.Queue()
        self.dest_queue = queue.Queue()
        self.src_visited = set()
        self.dest_visited = set()
        self.init_state = init_state
        self.goal_state = goal_state
        self.heuristic = heuristic
    
    
    def solve(self):
        debut_node = Node(self.init_state,self.goal_state,heuristic=self.heuristic)
        goal_node = Node(self.goal_state,self.init_state,heuristic=self.heuristic)
        self.src_queue.put(debut_node)
        self.dest_queue.put(goal_node)
        queue_src_size = []
        queue_dest_size = []
        while not (self.src_queue.empty() or self.dest_queue.empty()):
            #Checking if a common state is found
            if len(self.src_visited.intersection(self.dest_visited)) != 0:
                print("ok")
                break
            queue_src_size.append(self.src_queue.qsize())
            popped_node = self.src_queue.get()
            if popped_node.state not in self.src_visited:
                self.src_visited.add(popped_node.state)
                neighbours = popped_node.expand()
                for son in neighbours:
                    if son.state in self.src_visited:
                        continue
                    self.src_queue.put(son)
            queue_dest_size.append(self.dest_queue.qsize())
            popped_node = self.dest_queue.get()
            if popped_node.state not in self.dest_visited:
                self.dest_visited.add(str(popped_node.state))
                neighbours = popped_node.expand()
                for son in neighbours:
                    if son.state in self.dest_visited:
                        continue
                    self.dest_queue.put(son)
        max_number1,max_number2 = max(queue_src_size),max(queue_dest_size)
        return max_number1,max_number2


"""lis = [[1,2,3],[4,5,6],[7,8,0]]
print(lis[0][2])

solver = BiSearch([[1,2,3],[6,0,8],[5,4,7]],[[1,2,3],[4,5,6],[7,8,0]],"manhattan")
solver = BiSearch([[12,1,2,15],[11,6,5,8],[7,10,9,4],[0,13,14,3]],[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]],"manhattan")
solver.solve()
solver = BiSearch([[1,7,2,4],[6,10,8,3],[0,9,12,11],[13,5,14,15]],[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]],"manhattan")"""

