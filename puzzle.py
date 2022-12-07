import math

import copy
def check_if_square(n):
    if int(math.sqrt(n) + 0.01)**2 == n:
        return True
    else:
        return False

class Puzzle():
    def __init__(self,initial_state,goal_state):
        self.current_state = initial_state
        self.goal_state = goal_state
        self.dim = len(self.current_state)
        for i in range(len(self.current_state)):
            for j in range(len(self.current_state[i])):
                if self.current_state[i][j]==0:
                    self.empty_tile = [i,j]
                    break
    def __eq__(self,puzzle):
        same = True
        if self.dim == puzzle.dim:
            for i in range(self.dim):
                for j in range(self.dim):
                    if self.current_state[i][j] != puzzle.current_state[i][j]:
                        return False
                    break
        return True
    def copy(self):
        return type(self)(self.current_state, self.goal_state)
                
            
    
    def show_game(self):
        print("Current state of the game : \n")
        for i in range(len(self.current_state)):
            for j in range(len(self.current_state[i])):
                if self.current_state[i][j]:
                    print("[" + str(self.current_state[i][j]) + "]",end ="")
                else:
                    print("[ ]",end="")
                print(",",end="")
            print("\n")
    
    
    
    
    def available_actions(self):
        x,y = self.empty_tile
        available_actions = []
        #Checking if we are in the corners
        #Up
        up,down,left,right = False,False,False,False
        if x == 0:
            up = True
        if x == self.dim -1:
            down = True
        if y == self.dim -1:
            right = True
        if y == 0:
            left = True
        if not up:
            #Move empty tile up
            available_actions.append([x-1,y])
        if not down:
            #Move empty tile down
            available_actions.append([x+1,y])
        if not left:
            available_actions.append([x,y-1])
        if not right:
            available_actions.append([x,y+1])
        
        return available_actions
    
    def act(self,action):
        tmp = copy.deepcopy(self.current_state)
        for i in range(len(tmp)):
            for j in range(len(tmp[i])):
                if [i,j] == self.empty_tile:
                    tmp[i][j] = tmp[action[0]][action[1]]
                    tmp[action[0]][action[1]] = 0
                    break
        return Puzzle(tmp,copy.deepcopy(self.goal_state))
    
        
        
pz = Puzzle([[2,1],[3,0]],[[2,1],[3,0]])
print(pz.show_game())
print(pz.available_actions())
st = []
for elem in pz.available_actions():
    st.append(pz.act((elem)))
for elem in st:
    print(elem.show_game())
print(pz.show_game())