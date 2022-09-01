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
R = int(input())
As = [int(item) for item in input().split()]


if N == 1:
    print(As[0])
else:
    res = []
    anchor = 0
    prev = As[0]
    for i in As[1:]:
        print(i, anchor)
        if anchor == 0 and i - As[0] > R:
            res.append(prev)
            anchor = prev
        
        if i - anchor > R:
            res.append(i)
            anchor = i 
        prev = i

print(res)

