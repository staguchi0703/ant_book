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
#
# 以下ペースト可

N, M = [int(item) for item in input().split()]

to_lists = [[int(item) for item in input().split()] for _ in range(M)]

costs = [0 for _ in range(N+1)]
cnt = 0
while True:
    for i in range(M):
        from_indx, to_indx, cost = to_lists[i]
        costs[to_indx] = max([costs[to_indx], costs[from_indx] + cost])
        cnt += 1
    if cnt > N:
        break
print(max(costs))