import sys
input = sys.stdin.readline

n = int(input())
count = [0]*10001  # 0~10000번까지

for _ in range(n):
    count[int(input())] += 1  # 들어오는 숫자의 개수 올리기
    
for i in range(10001):
    if count[i] != 0:  # 개수가 0이 아닐 때
        for _ in range(count[i]):
            print(i)  # 개수 출력