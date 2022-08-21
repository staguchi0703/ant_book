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
H, W = [int(i) for i in input().split()]

grid =[
        [int(i) for i in input().split()]
        for _ in range(H)
      ] 

def get_holi(i, j):
    line = grid[i]
    return sum(line)

def get_ver(i, j):
    sum = 0
    for line in grid:
        tmp = line[j]
        sum += tmp
    return sum

def get_site_value(i, j):
    return get_holi(i,j) + get_ver(i,j) - grid[i][j]

for i in range(H):
    line = [get_site_value(i, j) for j in range(W)]
    print(*line)


