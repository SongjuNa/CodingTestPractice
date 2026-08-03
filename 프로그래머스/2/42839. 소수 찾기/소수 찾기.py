from itertools import permutations # 순열 모듈 사용
def solution(numbers):
    
    count = 0
    unique_nums = set()  # 집합으로 중복 제거
    for i in range(1, len(numbers)+1):
        for p in permutations(numbers, i):  # 소수 생성
            num = int(''.join(p))
            unique_nums.add(num)
    
    for num in unique_nums:
        if num < 2:
            continue
        
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
    return count