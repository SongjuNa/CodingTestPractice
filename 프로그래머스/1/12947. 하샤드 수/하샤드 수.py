def solution(x):
    x = str(x)
    total = 0
    
    for i in range(len(x)):
        total += int(x[i])
    if int(x) % total == 0:
        answer = True
    else:
        answer = False
    return answer