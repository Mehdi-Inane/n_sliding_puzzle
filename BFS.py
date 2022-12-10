from node import *
from queue import *
from puzzle import *
import sys
sys.setrecursionlimit(1000000)
from queue import Queue

class BFS:
	
	def __init__(self,init_state,goal_state):
		self.init_state = init_state
		self.goal_state = goal_state
				
	def solve(self):
		visited=set()
		queue=Queue()
		debut_node=Node(self.init_state,self.goal_state,heuristic=None)
		queue.put(debut_node)
		visited.add(str(debut_node.state))
		parent = dict()
		parent[str(self.init_state)] = None
		path_found = False
		while not queue.empty():
			popped_node = queue.get()
			#popped_node.state.show_game()
			if popped_node.state.is_goal_state():
				print("okBFS")
				path_found = True
				break
			for node_next in popped_node.expand():
				if str(node_next.state) not in visited:
					queue.put(node_next)
					
					parent[str(node_next.state)] = popped_node
					visited.add(str(node_next.state))
                	
        #PATH RECONSTRUCITON        	
		#path = []
		#if path_found:
			#path.append(self.goal_state)
			#print(parent[str(self.goal_state)])
			#while parent[str(self.goal_state)] is not None:
				#path.append(str(parent[str(self.goal_state)].state)) 
				#self.goal_state = parent[str(self.goal_state)]
			#path.reverse()
		#for p in path:
			#print(p)
		#return path 
    	#for (node_next, w) in self.m_adj_list[current_node]:
    	
#solver = BFS([[12,1,2,15],[11,6,5,8],[7,10,9,4],[0,13,14,3]],[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]])
solver = BFS([[0,3,6],[1,7,2],[5,4,8]],[[1,2,3],[4,5,6],[7,8,0]])
#solver = Astar([[5,3,6],[2,1,8],[0,4,7]],[[1,2,3],[4,5,6],[7,8,0]])
solver.solve()
