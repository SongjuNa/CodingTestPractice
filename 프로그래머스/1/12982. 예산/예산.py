# 그리디 탐색/정렬 기초 문제!

def solution(d, budget):
    result = 0
    d.sort()
    
    for num in d:
        if num <= budget:
            budget -= num
            result += 1
        else:
            break

    return result