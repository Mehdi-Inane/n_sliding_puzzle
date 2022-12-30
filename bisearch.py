
import queue
from node import *
from puzzle import *
import sys
sys.setrecursionlimit(1000000)
class BiSearch:


    def __init__(self,init_state,goal_state,heuristic):
        #Source frontier
        self.src_queue = queue.Queue()
        #Destination frontier
        self.dest_queue = queue.Queue()
        #Sets of closed states
        self.src_visited = set()
        self.dest_visited = set()
        self.init_state = init_state
        self.goal_state = goal_state
        self.heuristic = heuristic
    
    
    def solve(self,show_path = False):
        debut_node = Node(self.init_state,self.goal_state,heuristic=self.heuristic)
        goal_node = Node(self.goal_state,self.init_state,heuristic=self.heuristic)
        self.src_queue.put(debut_node)
        self.dest_queue.put(goal_node)
        queue_src_size = []
        queue_dest_size = []
        while not (self.src_queue.empty() or self.dest_queue.empty()):
            #Checking if a common state is found --> A path exists
            intersection = self.src_visited.intersection(self.dest_visited)
            if len(intersection) != 0:
                if show_path:
                    meeting_state = intersection.pop()
                    left_path_start = self.src_dict[meeting_state]
                    right_path_start = self.dest_dict[meeting_state]
                    #Displaying the path
                    print(show_path_two_sides(left_path_start,right_path_start))
                break
            queue_src_size.append(self.src_queue.qsize())
            #Starting the search from the source node
            popped_node = self.src_queue.get()
            if popped_node.state not in self.src_visited:
                self.src_visited.add(popped_node.state)
                neighbours = popped_node.expand()
                for son in neighbours:
                    if son.state in self.src_visited:
                        continue
                    self.src_queue.put(son)
            queue_dest_size.append(self.dest_queue.qsize())
            #Starting the search from the goal node
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