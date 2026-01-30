def solution(n):
    answer = '' #문자열

    while n>0:
        remainder = n % 3
        n = n//3
        answer += str(remainder)
    
    return int(answer, 3) # 3진법 알아서 10진법으로 변환