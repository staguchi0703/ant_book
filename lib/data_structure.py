##################################################
# heap
###################################################
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


####################################################
# union-find
####################################################

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
    
    
def main() -> None:
    n, m = map(int, input().split())

    uf = UnionFind(n)

    for _ in range(m):
        a, b = map(int,input().split())
        uf.merge(a - 1, b - 1)

    ans = 0
    for i in range(n):
        ans = max(ans, uf.size(i))

    print(ans)

if __name__ == "__main__":
    main()