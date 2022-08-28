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
N, M = [int(i) for i in input().split()]
grid = [[i for i in input()] for _ in range(N) ]



def paint(i,j):
    grid[i][j] = "."

    for ni in [-1, 0, 1]:
        for nj in [-1, 0, 1]:
            nx = i + ni
            ny = j + nj
            if (0 <= nx <= M-1) and (0 <= ny <= N-1):
                if grid[ny][nx] == "w":
                    print(ny, nx)
                    paint(ny, nx)

def search(i,j):
    if grid[i][j] == "w":
        paint(i, j)
        return 1
    else:
        return 0

cnt = 0
for i in range(N):
    for j in range(M):
        print("-"*30)
        print(i, j)
        pprint(grid)
        cnt += search(i, j)

print(cnt)