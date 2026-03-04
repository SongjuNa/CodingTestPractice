n = int(input())
a = [0]*n

for i in range(n):
    a[i] = int(input())
    
stack = []  # 숫자 담아둘 스택
num = 1   # 스택에 넣을 차례인 숫자
result = True  # 수열을 만들 수 있는지 여부
answer = []  # '+'와 '-' 기호를 저장할 리스트

for i in range(n):
    su = a[i]    # 현재 수열에서 꺼내야 하는 숫자
    if su >= num:  # 뽑아야 할 숫자가 아직 스택에 안들어왔거나 막 들어오려고 하면
        while su >= num:   # 그 숫자가 나올 때까지 1씩 증가시키면서 스택에 삽입
            stack.append(num)
            num += 1
            answer.append('+')  # 삽입할 때마다 '+' 기록
        stack.pop()  # 목표 숫자까지 다 넣었으면 맨 위 숫자 꺼냄
        answer.append('-')  # 꺼낼 때마다 '-' 기록
    else:  # 뽑아야 할 숫자가 스택에 있다면
        n = stack.pop()  # 스택의 맨 위 숫자 꺼내서 확인
        if n > su:   # 꺼낸 숫자가 내가 뽑으려던 숫자보다 크면
            print("NO")  # 수열 만들 수 없음
            result = False 
            break
        else:
            answer.append('-')  # 꺼낸 숫자가 목표값과 같다면 '-' 기록
            
if result:  # 수열 만드는 데 성공했다면
    for i in answer:
        print(i)   # answer 리스트 내의 원소들 출력