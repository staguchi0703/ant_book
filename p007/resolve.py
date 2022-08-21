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
def resolve():
    '''
    code here
    '''
    from bisect import bisect_left

        
    N = int(input())
    As = [int(i) for i in input().split()]
    Q = int(input())
    Bs =[int(input()) for _ in range(Q)]

    As.sort()

    def res_val(As, b):
        j = bisect_left(As, b)
        if j > 0:
            left = j -1
        else:
            left =j
        if j < N:
            right = j
        else:
            right = N-1                     
        # print(b, j,  As[left], As[j])
        return min(abs(As[left] -b), abs(As[right] -b))


    for b in Bs:
        print(res_val(As, b))
if __name__ == "__main__":
    resolve()