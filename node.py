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
    


node = Node(Puzzle([[2,1],[3,0]],[[2,1],[3,0]]),heuristic = 1)
new_nodes = node.expand()
print(new_nodes)
for node in new_nodes:
    print(node.state.show_game())

            



