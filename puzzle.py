import math
from operator import length_hint 
from colorama import Fore, Back, Style
import numpy as np



def find_elem(mat,elem):
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j]==elem:
                return i,j
    return None 

import copy
import random
def check_if_square(n):
    if int(math.sqrt(n) + 0.01)**2 == n:
        return True
    else:
        return False

class Puzzle():
    def __init__(self,initial_state,goal_state,nb_iter = 0,parent_puzzle= None,heuristic = "manhattan"):
        self.current_state = initial_state
        self.goal_state = goal_state
        self.heuristic = heuristic
        self.dim = initial_state.shape[0]
        for i in range(self.dim):
            for j in range(self.dim):
                if self.current_state[i][j]==0:
                    self.empty_tile = [i,j]
                    break

    def __eq__(self,puzzle):
        return np.array_equal(self.current_state,puzzle.current_state)
                
    def is_goal_state(self):
        return np.array_equal(self.current_state,self.goal_state)
    
    def __str__(self):
        return str(self.current_state)

    
    
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
        tmp = np.copy(self.current_state)
        i,j = self.empty_tile[0],self.empty_tile[1]
        tmp[i][j] = tmp[action[0]][action[1]]
        tmp[action[0]][action[1]] = 0
        return Puzzle(tmp,self.goal_state)


    def print_puzzle(self):
        left_down= '\u2514'
        right_down= '\u2518'
        right_up= '\u2510'
        left_up = '\u250C'
        middle = '\u253C'
        top = '\u252C'
        bottom= '\u2534'
        right= '\u2524'
        left= '\u251C'
            
            #line color
        line = Style.BRIGHT + Fore.GREEN+ '\u2502' + Fore.RESET + Style.RESET_ALL
        dash = '\u2500'

            #Line draw code
        f_line = Style.BRIGHT  + Fore.GREEN+ left_up + dash + dash + dash +(top+ dash + dash + dash)*(len(self.current_state)-1) + right_up + Fore.RESET + Style.RESET_ALL

        m_line = Style.BRIGHT + Fore.GREEN+ left + dash + dash + dash + (middle+ dash + dash + dash)*(len(self.current_state)-1) + right+ Fore.RESET + Style.RESET_ALL

        l_line = Style.BRIGHT + Fore.GREEN + left_down + dash + dash + dash + (bottom+ dash + dash + dash)*(len(self.current_state)-1)  + right_down + Fore.RESET + Style.RESET_ALL
        print(f_line)
        for i in range(len(self.current_state)):
            for j in self.current_state[i]:
                if j == 0:
                    print(line, Back.WHITE + ' ' + Back.RESET, end=' ')
                else:
                    print(line, j, end=' ')
            print(line)
            if i == len(self.current_state)-1:
                print(l_line)
            else:
                print(m_line)

def get_goal_state(nb_tiles):
        #Starting from the goal state
    init_state = []
    cpt = 1
    for i in range(nb_tiles):
        init_state.append([])
        for j in range(nb_tiles):
            if (i == nb_tiles -1) and (j == nb_tiles -1):
                init_state[i].append(0)
                break
            init_state[i].append(cpt)
            cpt += 1
    return np.array(init_state)
   
                


def generate_random(nb_tiles,nb_moves):
    init_state = get_goal_state(nb_tiles)
    goal_state = np.copy(init_state)
    puz = Puzzle(init_state,goal_state)
    #Generating random actions
    visited_states = set()
    visited_states.add(str(puz))
    for i in range(nb_moves):
        while(str(puz) in visited_states):
            actions = puz.available_actions()
            rand_action = actions[random.randint(0,len(actions) - 1)]
            puz = puz.act(rand_action)
        visited_states.add(str(puz))
    return puz

