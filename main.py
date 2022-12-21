from Astar import *
from bisearch import *
from puzzle import *
from bi_search_astar import *
from BFS import *
import time
import numpy as np


def main():
    print("Do you want to generate a random puzzle (1) or input a puzzle (2)")
    i = int(input())
    print("How many tiles (n*n) ?")
    nb_tiles = int(input())
    if i == 1:
        print("How many shuffles ?")
        nb_shuffles = int(input())
        puzzle = generate_random(nb_tiles,nb_shuffles)
        init_state = puzzle.current_state
        goal_state = puzzle.goal_state
    else:
        print("Do you want to write your puzzle on the terminal (1) or input a puzzle from a file (2)")
        c = int(input())
        if c==1:
            print("For each row of the puzzle, input the numbers separated by spaces then press enter")
            init_state = []
            for i in range(nb_tiles):
                row = input()
                row = row.split()
                init_state.append([])
                for j in range(nb_tiles):
                    init_state[i].append(int(row[j]))
            init_state = np.array(init_state)
            goal_state = get_goal_state(nb_tiles)
        else:
            init_state = np.loadtxt('file.txt').astype(int)
            if(nb_tiles!= len(init_state)):
                print("The size of the puzzle in your file should correspond to the number of tiles you have chosen, modify your file or start again with the corresponding number of tiles")
                return 
            goal_state = get_goal_state(nb_tiles)
    print("Which heuristic ? manhattan / misplaced_tiles/ 0 {for no heuristic -> UCS}")
    heuristic = input()
    print("Compare algorithms (1) or find a solution (2) ?")
    i = int(input())
    if i ==2:
        print("What algorithm do you want to use ? 1 - A* 2 - Bidirectional search BFS 3- Bidirectional search A* 4- BFS")
        i = int(input())
        if i == 1:
            solver = Astar(init_state,goal_state,heuristic)
        elif i == 2:
            solver = BiSearch(init_state,goal_state,heuristic)
        elif i ==3:
            solver = BiSearchA(init_state,goal_state,heuristic)
        else:
            solver = BFS(init_state,goal_state)
        start = time.time()
        solver.solve()
        end = time.time()
        print("elapsed time : ",end - start)
    else:
        solver_1 = Astar(init_state,goal_state,heuristic)
        start = time.time()
        max_queue=solver_1.solve()
        end = time.time()
        print("elapsed time for A*:",end-start)
        print("space complexity ; max frontier size for A*:",max_queue)
        solver_2 = BiSearchA(init_state,goal_state,heuristic)
        start = time.time()
        max_queue=solver_2.solve()
        end = time.time()
        print("elapsed time for BiSearch A*:",end-start)
        print("space complexity ; max frontier size for BiSearch BFS for frontier1:",max_queue[0])
        print("space complexity ; max frontier size for BiSearch BFS for frontier2:",max_queue[1])
        solver_2 = BiSearch(init_state,goal_state,heuristic)
        start = time.time()
        max_queue=solver_2.solve()
        end = time.time()
        print("elapsed time for BiSearch BFS:",end-start)
        print("space complexity ; max frontier size for BiSearch BFS for frontier1:",max_queue[0])
        print("space complexity ; max frontier size for BiSearch BFS for frontier2:",max_queue[1])
        solver_2 = BFS(init_state,goal_state)
        start = time.time()
        max_queue=solver_2.solve()
        end = time.time()
        print("elapsed time for BFS:",end-start)
        print("space complexity ; max frontier size for BFS:",max_queue)


            


main()