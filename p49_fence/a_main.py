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

N = int(input())
As = [int(item) for item in input().split()]

import heapq as hq

hq.heapify(As)

res = 0
for _ in range(N-1):
    min_item = hq.heappop(As)
    second_min_item = hq.heappop(As)

    t = min_item + second_min_item
    res += t
    print(min_item, second_min_item, res)
    hq.heappush(As, t)

print(res)