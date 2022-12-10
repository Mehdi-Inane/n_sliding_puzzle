from priorityqueue import *
from node import *
from puzzle import *
from BST import * 
import sys
sys.setrecursionlimit(1000000)

class Astar:

    def __init__(self,init_state,goal_state,heuristic):
        self.init_state = init_state
        self.goal_state = goal_state
        self.heuristic = heuristic

    def solve(self):
        explored_states = set()
        pt_queue = PriorityQueue()
        debut_node = Node(self.init_state,self.goal_state,heuristic=self.heuristic)
        pt_queue.insert(debut_node)
        while not pt_queue.isEmpty():
            popped_node = pt_queue.pop()
            
            #If the node was already explored
            if str(popped_node.state) in explored_states:
                continue
            else:
                explored_states.add(str(popped_node.state))
                #popped_node.state.show_game()
            
            #If the node contains the goal state
            if popped_node.state.is_goal_state():
                print("ok")
                break
            neighbours = popped_node.expand()
            for son in neighbours:
                pt_queue.insert(son)


#"manhattan"
#"misplaced_tiles"
solver = Astar([[12,1,2,15],[11,6,5,8],[7,10,9,4],[0,13,14,3]],[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]],"manhattan")
#solver = Astar([[0,3,6],[1,7,2],[5,4,8]],[[1,2,3],[4,5,6],[7,8,0]],"misplaced_tiles")
#solver = Astar([[5,3,6],[2,1,8],[0,4,7]],[[1,2,3],[4,5,6],[7,8,0]],"manhattan")
solver.solve()

            

