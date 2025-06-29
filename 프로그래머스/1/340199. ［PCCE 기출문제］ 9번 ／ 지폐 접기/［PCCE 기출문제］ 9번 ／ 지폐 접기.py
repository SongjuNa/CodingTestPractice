def solution(wallet, bill):
    answer = 0
    w0, w1 = wallet
    b0, b1 = bill
    
    while True:
        if (b0 <= w0 and b1 <= w1) or (b0 <= w1 and b1 <= w0):
            break
            
        if b0 > b1:
            b0 //= 2
        else:
            b1 //= 2
        answer += 1
        
    return answer