import queue
from node import *
from puzzle import *
from BST import * 
import sys
sys.setrecursionlimit(1000000)

class BiSearchA:
    def __init__(self,init_state,goal_state,heuristic):
        self.src_queue = queue.PriorityQueue()
        self.dest_queue = queue.PriorityQueue()
        self.src_visited = set()
        self.dest_visited = set()
        self.init_state = init_state
        self.goal_state = goal_state
        self.heuristic = heuristic
    

    def solve(self):
        debut_node = Node(self.init_state,self.goal_state,heuristic=self.heuristic)
        goal_node = Node(self.goal_state,self.init_state,heuristic=self.heuristic)
        self.src_queue.put((0,debut_node))
        self.dest_queue.put((0,goal_node))
        queue_src_size = []
        queue_dest_size = []
        while not (self.src_queue.empty() or self.dest_queue.empty()):
            #Checking if a common state is found
            if len(self.src_visited.intersection(self.dest_visited)) != 0:
                print("ok")
                break
            queue_src_size.append(self.src_queue.qsize())
            popped_node = self.src_queue.get()[1]
            if str(popped_node.state) not in self.src_visited:
                self.src_visited.add(str(popped_node.state))
                neighbours = popped_node.expand()
                for son in neighbours:
                    if str(son.state) in self.src_visited:
                        continue
                    self.src_queue.put((son.n,son))
            queue_dest_size.append(self.dest_queue.qsize())
            popped_node = self.dest_queue.get()[1]
            if str(popped_node.state) not in self.dest_visited:
                self.dest_visited.add(str(popped_node.state))
                neighbours = popped_node.expand()
                for son in neighbours:
                    if str(son.state) in self.dest_visited:
                        continue
                    self.dest_queue.put((son.n,son))
        max_number1,max_number2 = max(queue_src_size),max(queue_dest_size)
        return max_number1,max_number2
