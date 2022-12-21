#from priorityqueue import *
from node import *
from puzzle import *
from BST import * 
import sys
sys.setrecursionlimit(1000000)
from queue import PriorityQueue

class Astar:

    def __init__(self,init_state,goal_state,heuristic):
        self.init_state = init_state
        self.goal_state = goal_state
        self.heuristic = heuristic

    def solve(self):
        explored_states = set()
        pt_queue = PriorityQueue()
        debut_node = Node(self.init_state,self.goal_state,heuristic=self.heuristic)
        pt_queue.put(debut_node)
        queuesize = []
        while not pt_queue.empty():
            queuesize.append(pt_queue.qsize())
            popped_node = pt_queue.get()
            #If the node was already explored
            if str(popped_node.state) in explored_states:
                continue
            else:
                explored_states.add(str(popped_node.state))            
            #If the node contains the goal state
            if popped_node.state.is_goal_state():
                print("ok")
                print(popped_node.state.show_game())
                print(show_family(popped_node))
                #Show the different steps to find the solution
                break
            neighbours = popped_node.expand()
            for son in neighbours:
                if str(son.state) in explored_states:
                    continue
                #pt_queue.insert(son)
                pt_queue.put(son)
        max_number = max(queuesize)
        return max_number
                
    def astar(self):
        exp=[]
        pt_queue = PriorityQueue()
        #explored_set = ()
        debut_node = Node(self.init_state,self.goal_state,heuristic=self.heuristic)
        pt_queue.put(debut_node)
        #while not pt_queue.empty():
        while(1):
            if pt_queue.qsize()==0:
                return None
            popped_node=pt_queue.get()
            #print(popped_node.state)
            if popped_node.state.is_goal_state() :
                
                #print("ok")
                #print(popped_node.state.show_game())
                #print(show_family(popped_node))
                return popped_node
                
            if (popped_node.isExp(exp) is None ) :
                exp.append(popped_node)
                neighbours = popped_node.expand()
                for son in neighbours:
                    if son.isExp(exp) is None:
                        pt_queue.put(son)
        return None 
        
    def solvee(self):
        """
        A* solver
        :param h_function: heurtic_function(Grid start, Grid goal)
        :return: path found to goal
        """
        open_set = PriorityQueue()  # stored ordered nodes by f value
        #open_set.put(Node(self.init_state,self.goal_state,heuristic=self.heuristic))
        debut_node=Node(self.init_state,self.goal_state,heuristic=self.heuristic)
        f = debut_node.state.calculate_fitness() + debut_node.state.nb_iter
        open_set.put(debut_node.state)
        
        closed_set = set()
        found = False
        while not open_set.empty():
            current= open_set.get()

            if current.is_goal_state():
                found = current
                break

            if str(current) in closed_set:
                continue

            closed_set.add(str(current))

            for child in current.expand_puzzle():
                #print(child)
                f = child.calculate_fitness()+ child.nb_iter
                open_set.put(child, f)
                
        if found:
            path = []
            while found:
                path.append(found)
                found = found.parent_puzzle
            path.reverse()

            print("Solution found")
            #for o in path :
               # print(o)
            #return path
            
        else:
            print("No solution found")

        
        
        
#"manhattan"
#"misplaced_tiles"
#solver = Astar([[1,2,3],[6,0,8],[5,4,7]],[[1,2,3],[4,5,6],[7,8,0]],"manhattan")
#solver = Astar([[0,3,6],[1,7,2],[5,4,8]],[[1,2,3],[4,5,6],[7,8,0]],"misplaced_tiles")
#solver = Astar([[5,3,6],[2,1,8],[0,4,7]],[[1,2,3],[4,5,6],[7,8,0]],"manhattan")
#solver = Astar([[12,1,2,15],[11,6,5,8],[7,10,9,4],[0,13,14,3]],[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]],"manhattan")
#solver = Astar([[12,1,2,15],[11,6,5,8],[7,10,9,4],[0,13,14,3]],[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]],"manhattan")
#solver = Astar([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,0,15]],[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]],"manhattan")
#solver.solve()
#solver.astar()
#solver.solvee()


            

