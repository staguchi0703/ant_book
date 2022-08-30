# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os

file_path = __file__.rsplit('\\',1)[0]
f=open(file_path + '/input.txt', 'r', encoding="utf-8")
# inputをフルパスで指定
# win10でファイルを作るとs-jisで保存されるため、読み込みをutf-8へエンコードする必要あり
# VScodeでinput file開くとutf8になってるんだけど中身は結局s-jisになっているらしい
sys.stdin=f

#
# 入力スニペット
# num = int(input())
# num_list = [int(item) for item in input().split()]
# num_list = [input() for _ in range(3)]
##################################
# %%
# 以下ペースト可
from pprint import pprint
import numpy as np
from collections import deque
N, M = [int(i) for i in input().split()]
maze = [[i for i in input()] for _ in range(N)]
d = [[np.inf for _ in range(M)] for _ in range(N)]


s_pos = []
is_s = False
for y in range(N):
    for x in range(M):
        if maze[y][x] == "S":
            s_pos = [x, y]
            is_s = True
        if is_s:
            break
    if is_s:
        break



g_pos = []
is_g = False
for y in range(N):
    for x in range(M):
        if maze[y][x] == "G":
            g_pos = [x, y]
            is_g = True
        if is_g:
            break
    if is_g:
        break

print(s_pos, g_pos)

def bfs(s_pos):
    q = deque([s_pos]) # s_posを一単位として初期化するため[]で囲う
    d[s_pos[1]][s_pos[0]] = 0

    while len(q) > 0:
        pos = q.popleft()
        for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
            nx, ny = pos[0] + dx, pos[1] + dy
            if (0<=nx<=M-1) and (0<=ny<=N-1):
                if maze[ny][nx] != "#" and d[ny][nx] == np.inf:
                    d[ny][nx] = d[pos[1]][pos[0]] + 1
                    q.append([nx, ny])
    return d

d = bfs(s_pos)
pprint(np.array(d))
print(d[g_pos[1]][g_pos[0]])