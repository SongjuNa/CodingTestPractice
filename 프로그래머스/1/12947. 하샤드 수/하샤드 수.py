def solution(x):
    x = str(x)
    
    total = 0
    for num in x:
        total += int(num)
    
    if int(x) % total == 0:
        answer = True
    else:
        answer = False
        
    return answer