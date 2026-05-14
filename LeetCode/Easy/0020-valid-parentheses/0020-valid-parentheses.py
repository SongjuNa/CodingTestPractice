class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {")": "(", "}": "{", "]": "["}
        stack = []
        
        for i in s:
            if i in mapping:  # i가 키인지(닫는 괄호인지)
                top = stack.pop() if stack else '#'  # 스택에 값이 있으면 가장 최근 값 꺼내고, 스택이 비었다면 더미 값 저장
                if mapping[i] != top:
                    return False
            else:
                stack.append(i)
                
        return not stack