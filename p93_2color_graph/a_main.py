# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
from pprint import pprint

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
num = int(input())
num_lists = [[int(item) for item in input().split()] for _ in range(num)]

colors = [0 for _ in range(num)]
g = []

for i, *to_list in num_lists:
    g.append(to_list)

print(g)

def dfs(v, c):
    colors[v] = c
    for to_index in g[v]:
        if colors[to_index] == c: return False
        if colors[to_index] == 0 and not dfs(to_index, -c): return False
    return True

def main():
    for i in range(num):
        if colors[i] == 0:
            if not dfs(i, 1):
                print("No")
                return
    print("YES")

if __name__ == "__main__":
    main()
            

        
        



