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


import heapq


N ,M, T = [int(i) for i in input().split(" ")]
As = [int(i) for i in input().split(" ")]
edges = [[int(i) for i in input().split(" ")] for _ in range(M)]

to_lists = [[] for _ in range(N)]
for v, to, c in edges:
    to_lists[v-1].append([to-1, c])

back_to_list = [[] for _ in range(N)]
for v, to, c in edges:
    back_to_list[to-1].append([v-1, c])

print("to list", to_lists)

INF = float('inf')
forward_costs = [INF for _ in range(N)]
backward_costs = [INF for _ in range(N)]

def dijk(costs, to_lists ,s):
    q = [[0, s]]
    heapq.heapify(q)
    cnt=0

    while len(q) > 0:
        cnt +=1
        cost, v = heapq.heappop(q)
        costs[v] = cost


        for to, c in to_lists[v]:
            if costs[v] + c <= costs[to]:
                costs[to] = c + costs[v]
                heapq.heappush(q, [costs[to], to])

    return costs


print(dijk(forward_costs, to_lists, 0))

print(dijk(backward_costs, back_to_list, 0))

total_move_cost = []
for i, j in zip(forward_costs, backward_costs):
    total_move_cost.append(i+j)

res_list = []
for i, mv_cost in enumerate(total_move_cost):
    cost = (T - mv_cost)*As[i]
    if cost >= 0:
        res_list.append(cost)

print(max(res_list))

