# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os

from numpy import Inf

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

N, W = [int(i) for i in input().split()]
V = N * 4
As = [[int(i)for i in input().split()] for _ in range(N)]

dp = [[Inf for _ in range(V+1)] for _ in range(N+1)]

dp[0][0] = 0


for i in range(N):
    w, v = As[i]
    for j in range(V+1):
        if j < v:
            dp[i+1][j] = dp[i][j]
        else:
            dp[i+1][j] = min(dp[i][j],
                             dp[i][j - v] + w
                        ) 
pprint(dp)
print("-"*20)

res = 0
for j in range(V+1):
    if dp[N][j] <= W:
        res = max(j, res)

print("res: ", res) 
