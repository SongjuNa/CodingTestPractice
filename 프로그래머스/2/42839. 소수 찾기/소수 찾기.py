from itertools import permutations #순열 모듈 사용
def solution(numbers):
    
    count = 0
    unique_nums = set()  #집합으로 중복 숫자 조합 제거
    
    #생성 가능한 모든 자릿수 순열
    for i in range(1, len(numbers)+1):
        for p in permutations(numbers, i): 
            num = int(''.join(p))
            unique_nums.add(num)
    
    #소수 판별
    for num in unique_nums:
        if num < 2: #0, 1은 소수 아니니까 패스
            continue
        
        is_sosu = True
        #2~(num-1)까지 나누어 떨어지는 수 있는지 체크
        for i in range(2, num):
            if num % i == 0:
                is_sosu = False #나누어 떨어지면 소수가 아니니까 break
                break
        if is_sosu:
            count += 1
    return count