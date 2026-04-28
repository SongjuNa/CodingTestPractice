def solution(numbers):
    nums = [str(x) for x in numbers]
    
    from functools import cmp_to_key
    
    def compare(x, y):
        if x + y > y + x:
            return -1 # x를 앞으로
        elif x + y < y + x:
            return 1  # y를 앞으로
        else:
            return 0
            
    nums.sort(key=cmp_to_key(compare))
    return str(int(''.join(nums)))