n = int(input())
a = list(map(int, input().split()))

answer = [0]*n
stack = []
for i in range(n):
    # 스택이 비어 있지 않으면서 현재 인덱스가 스택 top보다 클 경우
    while stack and a[stack[-1]] < a[i]:
        answer[stack.pop()] = a[i]  # 정답리스트에 현재 인덱스를 오큰수로 저장
    stack.append(i)  # while문 상관 없이 n번 반복마다 스택에 현재 인덱스 저장
        
while stack:   # 스택이 비어 있지 않다면(오큰수 못만난 수들) 빌 때까지
    answer[stack.pop()] = -1  # 스택에서 하나씩 빼면서 -1

print(*answer)