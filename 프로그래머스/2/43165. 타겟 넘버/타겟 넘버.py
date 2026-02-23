def solution(numbers, target):
    
    def dfs(index, current_sum): # index: 몇 번째 숫자, current_sum: 현재까지의 합계
        # index가 numbers 끝까지 다 돌면
        if index == len(numbers):
            if current_sum == target:
                return 1
            else:
                return 0
            
        # 아직 index가 numbers 다 돌지 않았으면
        # 덧셈으로 끝까지(경우의 수)
        plus = dfs(index + 1, current_sum + numbers[index])
        # 뺄셈으로 끝까지(경우의 수)
        minus = dfs(index + 1, current_sum - numbers[index])
        
        # 덧셈방법 + 뺄셈방법(경우의 수 합)
        return plus + minus
    # dfs가 0번째 숫자부터 합계 0부터 시작
    return dfs(0, 0)