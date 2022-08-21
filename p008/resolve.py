def resolve():
    '''
    code here
    '''

    N = int(input())
    S = input()

    chk = "atcoder"

    res = 1

    for i in chk:
        cnt = 0
        for j in S:
            if i==j:
                cnt += 1
        if cnt !=0:
            res *= cnt
            res %= (10**9 + 7)

    print(res)

if __name__ == "__main__":
    resolve()
