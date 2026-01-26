def solution(nums):
    pick = len(nums) // 2
    kind = len(set(nums)) #set으로 중복 자동제거
    
    return min(pick, kind)