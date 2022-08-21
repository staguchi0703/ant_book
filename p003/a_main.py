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
from collections import deque

N = int(input())
edge_list = [[int(item) for item in input().split()] for _ in range(N-1)]

def get_to_list(edges):
    to_list = [[] for _ in range(N+1)]
    for f, t in edges:
        to_list[f] += [t]
        to_list[t] += [f]
    return to_list

def dist(start):
    to_list = get_to_list(edge_list)

    dist_list = [-1 for _ in range(N+1)]

    que = deque([])
    que.append(start)
    dist_list[start] = 0

    while len(que) > 0:
        site = que.popleft()
        for next in to_list[site]:
            if dist_list[next] == -1:
                dist_list[next] = 1 + dist_list[site]
                que.append(next)
    return dist_list

first_dist = dist(1)
max_val = max(first_dist)
max_index = first_dist.index(max_val)


res = max(dist(max_index))
print(res + 1)