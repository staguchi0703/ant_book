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

    N = int(input())
    S = input()

    chk = "atcoder"
    mod = 10**9+7

    dp =[[0 for _ in range (N+1)] for _ in range(len(chk)+1)]

    dp[0][0] = 1

    for i, i_val in enumerate(chk):
        for j in range(len(S)+1):
            if j < len(S):
                if i_val == S[j]:
                    dp[i+1][j+1] += dp[i][j]
                    print("True")
                else:
                    dp[i][j+1] += dp[i][j]
                    print("False")
                    print(dp[i])
   
    print(dp)
    print(dp[6][N])

if __name__ == "__main__":
    resolve()


# %%
