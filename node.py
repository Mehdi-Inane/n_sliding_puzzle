from puzzle import *


class Node():
    def __init__(self,state,action = None,nb_iter = 0,parent_node= None,heuristic = 0):
        self.state = state
        self.action = action
        self.n = nb_iter
        self.parent_node = parent_node
        self.heuristic = heuristic
    
    def expand(self):
        available_actions = self.state.available_actions()
        node_list = []
        for action in available_actions:
            state = self.state.act(action)
            node_list.append(Node(state,action,self.n +1,self,self.heuristic))
        return node_list
    
    def heuristicNull(self):
        return 0

    def manhattan(self, x1, y1, x2, y2):
            return abs(x1 - x2) + abs(y1 - y2)
                
    #number of displaced tiles     
    def calculate_fitness(self):
            if self.heuristic== "misplaced_tiles":
                for current_state, goal_state in zip(self.state.current_state, self.state.goal_state):
                    if current_state != current_state:
                        self.n+= 1
            elif self.heuristic == "manhattan":
                for current_state in self.state:
                    current_index = self.state.index(current_state)
                    goal_index = self.goal_state.index(current_state)
                    cur_i, cur_j = current_index // int(np.sqrt(len(self.state))), current_index % int(np.sqrt(len(self.state)))
                    goal_i, goal_j = goal_index// int(np.sqrt(len(self.state))), goal_index % int(np.sqrt(len(self.state)))
                    self.n += self.manhattan(cur_i, cur_j, goal_i, goal_j)
            else:
                print('Unknown heuristic function is being used.')


node = Node(Puzzle([[2,1],[3,0]],[[2,1],[3,0]]),heuristic = 1)
new_nodes = node.expand()
print(new_nodes)
for node in new_nodes:
    print(node.state.show_game())

            



