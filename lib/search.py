###########################################################
# DFS
###########################################################
class DFS:
    def __init__(self, w, h):
        self.grid = [[i for i in w] for _ in range(h) ]
        self.w = w
        self.h = h
        self.cnt = 0


    def search(self, y, x, target):
        self.grid[y][x] = "."

        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                ny = y + dy
                nx = x + dx
                if (0 <= nx < self.w) and (0 <= ny < self.h):
                    if self.grid[ny][nx] == target:
                        self.cnt += 1
                        self.search(ny, nx)

###########################################################
# BFS
###########################################################
import numpy as np
from collections import deque

class BFS:
    def __init__(self, M, N, maze, wall) -> None:
        self.maze = maze
        self.d = [[np.inf for _ in range(M)] for _ in range(N)]
        self.M = M
        self.N = N
        self.wall = wall

    def search(self, s_pos):
        q = deque([s_pos]) # s_posを一単位として初期化するため[]で囲う
        self.grid[s_pos[1]][s_pos[0]] = 0

        while len(q) > 0:
            pos = q.popleft()
            for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
                nx, ny = pos[0] + dx, pos[1] + dy
                if (0<=nx<self.M) and (0<=ny<self.N):
                    if self.maze[ny][nx] != self.wall and self.d[ny][nx] == np.inf:
                        self.d[ny][nx] = self.d[pos[1]][pos[0]] + 1
                        q.append([nx, ny])
        return self.d
    

##############################################################
# bit search
##############################################################

item = ["a", "b", "c", "d"]
n = len(item)
for i in range(2 ** n):
    bag = []
    print("pattern {}: ".format(i), end="")
    for j in range(n):  # このループが一番のポイント
        if ((i >> j) & 1):  # 順に右にシフトさせ最下位bitのチェックを行う
            bag.append(item[j][0])  # フラグが立っていたら bag に果物を詰める
    print(bag)