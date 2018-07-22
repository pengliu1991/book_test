#!/usr/bin/env python
# -*- coding:utf-8 -*-

#---*迷宫问题d*----
import sys

reload(sys)
sys.setdefaultencoding('utf8')

maze1 = [
  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
  [1,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,1],
  [1,0,0,0,0,1,0,1,0,1,0,1,1,0,1,0,1,1,0,1],
  [1,1,1,1,1,1,0,1,0,1,0,0,0,0,1,0,0,0,0,1],
  [1,0,0,0,1,0,0,1,1,1,0,1,1,1,1,1,1,1,1,1],
  [1,1,1,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,1,0,1,0,1,1,1,0,1,1,1,1,1,1,0,1],
  [1,1,1,0,1,0,1,0,1,0,0,0,1,0,0,0,0,1,0,1],
  [1,0,0,0,0,0,1,0,1,0,1,1,1,0,1,1,0,1,0,1],
  [1,0,1,0,1,1,1,0,1,0,1,0,0,0,1,1,1,1,0,1],
  [1,0,1,0,1,0,0,0,1,0,1,0,1,0,0,1,0,0,0,1],
  [1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,1,0,1],
  [1,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,1],
  [1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1],
  [1,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,1],
  [1,1,1,1,0,1,1,1,0,1,0,1,1,1,0,1,0,1,0,1],
  [1,0,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,1],
  [1,0,1,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1],
  [1,0,0,1,0,1,0,0,0,1,0,1,0,0,0,0,0,0,0,1],
  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

dirs = [(0,1), (1,0), (0,-1), (-1,0)]

def mark(maze, pos):
    maze[pos[0]][pos[1]] = 2

def passable(maze, pos):
    return maze[pos[0]][pos[1]] == 0

############################################
########## 递归求解 ####

def maze_solver_rec(maze, start, end):
    """ A maze solver using a recursive procedure to find the path.
    """
    def find_path(maze, start, end):
        mark(maze, start)
        if start == end:
            print(start)
            return True
        for i in range(4):
            nextp = start[0]+dirs[i][0], start[1]+dirs[i][1]
            if passable(maze, nextp):
                if find_path(maze, nextp, end):
                    print(start)
                    return True
        return False
    print("If find, print the path from end to start:")

    if find_path(maze, start, end):
        print("\n")
    else:
        print("No path exists.")

if __name__ == "__main__":
    maze_solver_rec(maze1, (1, 1), (18, 18))
