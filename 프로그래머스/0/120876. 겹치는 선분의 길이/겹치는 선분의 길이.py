def solution(lines):
    arr = [0] * 201
    
    for s, e in lines:
        for i in range(s, e):
            arr[i + 100] += 1
    
    # 2개 이상 겹치는 구간 수
    return sum(1 for x in arr if x >= 2)