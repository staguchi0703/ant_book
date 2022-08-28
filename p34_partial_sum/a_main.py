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
As = [int(i) for i in input().split()]
K = int(input())

As =  As

def recur(i, ttl):
    if i == len(As):
        return ttl == K
    else:
    
        if recur(i+1, ttl):
            return True

        if recur(i+1, ttl + As[i]):
            return True
        
        return False
        
print(recur(0, 0))
