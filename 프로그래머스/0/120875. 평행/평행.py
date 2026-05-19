def solution(dots):
    A = dots[0]  
    B = dots[1]   
    C = dots[2]
    D = dots[3]
    
    pairs = [
        (A, B, C, D),  # AB, CD
        (A, C, B, D),  # AC, BD
        (A, D, B, C)   # AD, BC
    ]
    
    for p1, p2, p3, p4 in pairs:
        if (p2[1] - p1[1]) * (p4[0] - p3[0]) == (p4[1] - p3[1]) * (p2[0] - p1[0]):
            return 1 
            
    return 0