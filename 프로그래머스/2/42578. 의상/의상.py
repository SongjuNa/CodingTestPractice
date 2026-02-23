def solution(clothes):
    closet = {}
    
    for c, type in clothes:
        closet[type] = closet.get(type, 0) +1
    
    answer = 1
    for count in closet.values():
        answer *= count +1
        
    return answer-1