def resolve():
    from collections import deque

    N = int(input())
    edge_list = [[int(item) for item in input().split()] for _ in range(N-1)]

    def get_to_list(edges):
        to_list = [[] for _ in range(N+1)]
        for f, t in edges:
            to_list[f] += [t]
            to_list[t] += [f]
        return to_list

    def dist(start):
        to_list = get_to_list(edge_list)

        dist_list = [-1 for _ in range(N+1)]

        que = deque([])
        que.append(start)
        dist_list[start] = 0

        while len(que) > 0:
            site = que.popleft()
            for next in to_list[site]:
                if dist_list[next] == -1:
                    dist_list[next] = 1 + dist_list[site]
                    que.append(next)
        return dist_list

    first_dist = dist(1)
    max_val = max(first_dist)
    max_index = first_dist.index(max_val)


    res = max(dist(max_index))
    print(res + 1)
if __name__ == "__main__":
    resolve()
