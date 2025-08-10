def solution(a, b, n):
    answer = 0
    
    while n // a >= 1:
        answer += (n//a) * b
        n = n - (a * (n//a)) + (n//a) * b
        print(answer, n)
    return answer