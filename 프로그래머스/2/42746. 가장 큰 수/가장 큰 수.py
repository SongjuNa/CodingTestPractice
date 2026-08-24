def solution(numbers):
    num = [str(i) for i in numbers]
    
    
    from functools import cmp_to_key
    
    def compare(i, j):
        if i+j > j+i: 
            return -1 #i 앞으로 
        elif i+j < j+i:
            return 1 #j 앞으로
        else:
            return 0 #순서 안바꿈
    
    num.sort(key=cmp_to_key(compare))
    return '0' if num[0] == '0' else ''.join(num)