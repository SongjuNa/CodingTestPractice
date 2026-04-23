from itertools import permutations
def solution(numbers):
    
    count = 0
    candidates = set()  # 중복제거(후보군 만들기)
    for i in range(1, len(numbers)+1):
        for p in permutations(numbers, i):  # 소수 생성
            num = int(''.join(p))
            candidates.add(num)
    
    for num in candidates:
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