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
        print("For each row of the puzzle, input the numbers separated by spaces then press enter")
        for i in range(nb_tiles):
            row = input()
            row = row.split()
            init_state = []
            init_state.append([])
            for j in range(nb_tiles):
                init_state[i].append(int(row[j]))
        init_state = np.array(init_state)
        goal_state = get_goal_state(nb_tiles)
    print("Which heuristic ? manhattan / misplaced_tiles")
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
        solver_1.solve()
        end = time.time()
        print("elapsed time for A*:",end-start)
        solver_2 = BiSearchA(init_state,goal_state,heuristic)
        start = time.time()
        solver_2.solve()
        end = time.time()
        print("elapsed time for BiSearch A*:",end-start)
        solver_2 = BiSearch(init_state,goal_state,heuristic)
        start = time.time()
        solver_2.solve()
        end = time.time()
        print("elapsed time for BiSearch BFS:",end-start)
        solver_2 = BFS(init_state,goal_state)
        start = time.time()
        solver_2.solve()
        end = time.time()
        print("elapsed time for BFS:",end-start)


            


main()