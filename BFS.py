from node import *
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
		path_found = False
		queuesize = []
		while not queue.empty():
			queuesize.append(queue.qsize())
			popped_node = queue.get()
			if str(popped_node.state) in visited:
				continue
			if popped_node.state.is_goal_state():
				print("ok")
				print(show_family(popped_node))
				path_found = True
				break
			for node_next in popped_node.expand():
				if str(node_next.state) not in visited:
					queue.put(node_next)
			visited.add(str(popped_node.state))
		max_number = max(queuesize)
		return max_number
    	
#solver = BFS([[12,1,2,15],[11,6,5,8],[7,10,9,4],[0,13,14,3]],[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]])
#solver = BFS([[0,3,6],[1,7,2],[5,4,8]],[[1,2,3],[4,5,6],[7,8,0]])
#solver = BFS([[5,3,6],[2,1,8],[0,4,7]],[[1,2,3],[4,5,6],[7,8,0]])
#solver.solve()

