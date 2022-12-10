from puzzle import *
import copy
def find_elem(mat,elem):
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j]==elem:
                return i,j
    return None 
    
class Node():
    def __init__(self,state,goal_state,action = None,nb_iter = 0,parent_node= None,heuristic = "manhattan"):
        self.state = Puzzle(state,goal_state)
        self.action = action
        self.n = nb_iter
        self.parent_node = parent_node
        self.heuristic = heuristic 
        self.calculate_fitness()
    
    def expand(self):
        available_actions = self.state.available_actions()
        node_list = []
        for action in available_actions:
            state = self.state.act(action)
            node_list.append(Node(state.current_state,goal_state = self.state.goal_state,action = action,nb_iter = copy.deepcopy(self.n) +1,parent_node = self,heuristic = self.heuristic))
        return node_list
    
    def __eq__(self,node):
        if self.state == node.state and self.action == node.action and self.n == node.n and self.parent_node == node.parent_node:
            return True
        return False
        
    def heuristicNull(self):
        return 0

    def manhattan(self, x1, y1, x2, y2):
            return abs(x1 - x2) + abs(y1 - y2)
           
                
    #number of displaced tiles     
    def calculate_fitness(self):
            if self.heuristic== "misplaced_tiles":
                for current_state, goal_state in zip(self.state.current_state, self.state.goal_state):
                    if current_state != goal_state:
                        self.n+= 1
            elif self.heuristic == "manhattan":
                for i in range(len(self.state.current_state )):
                    for j in range(len(self.state.current_state )):
                        x,y=find_elem(self.state.goal_state,self.state.current_state[i][j])
                        self.n+=self.manhattan(i, j, x, y) 
            else:
                self.n+=0
                #print('Unknown heuristic function is being used.')


"""node = Node(Puzzle([[2,1],[3,0]],[[2,1],[3,0]]),heuristic = 1)
new_nodes = node.expand()
print(new_nodes)
for node in new_nodes:
    print(node.state.show_game())"""

            



