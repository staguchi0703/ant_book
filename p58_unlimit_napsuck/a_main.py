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

N, W = [int(i) for i in input().split()]
As = [[int(i)for i in input().split()] for _ in range(N)]

dp = [[0 for _ in range(W+1)] for _ in range(N+1)]

for i in range(N):
    w, v = As[i]
    for j in range(W+1):
        if j >= w:
            dp[i+1][j] = max(dp[i+1][j-w] + v, dp[i][j]) 
        else:
            dp[i+1][j] = dp[i][j]

    pprint(dp)
    print("-"*20)

print(dp[N][W]) 
