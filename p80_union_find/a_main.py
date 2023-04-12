# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os

file_path = __file__.rsplit('\\',1)[0]
f=open(file_path + '/input.txt', 'r', encoding="utf-8")
sys.stdin=f

#
# 入力スニペット
# num = int(input())
# num_list = [int(item) for item in input().split()]
# num_list = [input() for _ in range(3)]
##################################
# %%
# 以下ペースト可

N, K = [int(item) for item in input().split()]
lines = [[int(item) for item in input().split()] for _ in range(K)]


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.p = [-1] * n


    def leader(self, a):
        while self.p[a] >= 0:
            a = self.p[a]
        return a


    def merge(self, a, b):
        x = self.leader(a)
        y = self.leader(b)

        if x == y:
            return x

        if self.p[x] > self.p[y]:
            x, y = y, x

        self.p[x] += self.p[y]
        self.p[y] = x

        return x

    def same(self, a, b):
        return self.leader(a) == self.leader(b)

    def size(self, a):
        return -self.p[self.leader(a)]
    
ans = 0
uf = UnionFind(3*N)

for t, x, y in lines:
    if 1 <= x <= N and 1 <= y <= N:
        if t == 1:
            if uf.same(x, y + N) or uf.same(x, y + 2*N):
                ans += 1
            else:
                for j in range(3):
                    uf.merge(x+j*N, y+j*N)

        else:
            if uf.same(x, y) or uf.same(x + N, y + N) or uf.same(x + 2*N, y + 2*N):
                ans += 1
            else:
                for j in range(2):
                    uf.merge(x, y + (j+1)*N) 
    else:
        ans +=1

print(ans)
    