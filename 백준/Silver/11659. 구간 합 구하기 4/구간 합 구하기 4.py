import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))

total = [0]
temp = 0
for k in num:
    temp += k
    total.append(temp)
    
for _ in range(m):
    i, j = map(int, input().split())
    print(total[j] - total[i-1])