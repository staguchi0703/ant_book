def resolve():
    '''
    code here
    '''
    N = int(input())
    total_num = 2**N
    top_bit = 2**N//2
    res_list = []
    
    for i in range(top_bit, total_num):
        chk = 0
        res=""
        for j in range(N):
            if ((i << j) & top_bit):
                chk += 1
                res += "("
            else:
                chk -= 1
                res +=")"
            
            if chk < 0:
                chk -= total_num                

        if ((i << (N-1)) & top_bit) != top_bit and chk == 0:
            res_list.append(res)
    res_list.sort()
    
    for item in res_list:
        print(item)

if __name__ == "__main__":
    resolve()
