from priorityqueue import *
from node import *
from puzzle import *
from BST import * 

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
            print("popped node",popped_node.state)
            #If the node was already explored
            if str(popped_node.state) in explored_states:
                print("already visited")
                print(pt_queue.tree.value)
                continue
            else:
                explored_states.add(str(popped_node.state))
            
            #If the node contains the goal state
            if popped_node.state.is_goal_state():
                print(popped_node.state.show_game())
                break
            neighbours = popped_node.expand()
            for son in neighbours:
                pt_queue.insert(son)
        if pt_queue:
            while pt_queue.tree.left or pt_queue.tree.right:
                if pt_queue.tree.left:
                    print(pt_queue.tree.left.value)
                if pt_queue.tree.right:
                    print(pt_queue.tree.right.value)


solver = Astar([[2,1],[0,3]],[[1,2],[3,0]],"")
solver.solve()

            

