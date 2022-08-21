def resolve():
    H, W = [int(i) for i in input().split()]

    grid =[
            [int(i) for i in input().split()]
            for _ in range(H)
        ] 

    def get_holi(i, j):
        line = grid[i]
        return sum(line)

    def get_ver(i, j):
        sum = 0
        for line in grid:
            tmp = line[j]
            sum += tmp
        return sum

    holi_list = [get_holi(i, 0) for i in range(H)]
    ver_list = [get_ver(0, j) for j in range(W)]
    for i in range(H):
        var_val = [ver_list[j] + holi_list[i] - grid[i][j] for j in range(W)]
        print(* var_val)
if __name__ == "__main__":
    resolve()
