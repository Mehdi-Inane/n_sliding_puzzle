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
        i = 0

        while not pt_queue.isEmpty() and i < 2:
            i += 1
            print("current content of the queue")
            curr = pt_queue.tree
            while curr:
                temp = curr
                curr.node.state.show_game()
                if curr.left:
                    curr = curr.left
                    curr.node.state.show_game()
                if temp.right:
                    curr = temp.right
                    curr.node.state.show_game()
            popped_node = pt_queue.pop()
            print("popped node",popped_node.state)
            #If the node was already explored
            if str(popped_node.state) in explored_states:
                continue
            else:
                explored_states.add(str(popped_node.state))
            
            #If the node contains the goal state
            if popped_node.state.is_goal_state():
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


solver = Astar([[1,2,4],[8,3,5],[6,7,0]],[[1,2,3],[4,5,6],[7,8,0]],"")
solver.solve()

            

