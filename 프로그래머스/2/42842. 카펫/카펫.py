def solution(brown, yellow):
    for w in range(1, yellow+1):
        if yellow % w == 0:
            h = yellow // w
            
            if w >= h and (w+2) * (h+2) - w*h == brown:
                return ([w+2, h+2])