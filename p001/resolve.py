def resolve():
    '''
    code here
    '''
    N = int(input())
    As = [int(input()) for _ in range(N)]

    my_list = [0] + As

    cnt = 1
    indx = my_list[1]
    res = -1
    while True:
        # print(indx)
        if cnt > N:
            break
        if indx == 2:
            res = cnt
            break
        
        indx = my_list[indx]
        cnt += 1

    print(res)


if __name__ == "__main__":
    resolve()


def resolve():
    '''
    code here
    '''
    N = int(input())
    a_list = [int(input()) for _ in range(N)]
 
    is_not_found = True
    cnt = 1
    idx = a_list[0] - 1
    while is_not_found:
        if idx == 1:
            is_not_found = False
            print(cnt)
        elif cnt >= N:
            is_not_found = False
            print(-1)
        
        idx = a_list[idx] - 1
        cnt += 1
 
 
if __name__ == "__main__":
    resolve()