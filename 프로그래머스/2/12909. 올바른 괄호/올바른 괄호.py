def solution(s):
    score = 0
    
    for i in s:
        if i == '(':
            score += 1
        else:
            score -= 1
        
        if score < 0:
            return False
    return score == 0