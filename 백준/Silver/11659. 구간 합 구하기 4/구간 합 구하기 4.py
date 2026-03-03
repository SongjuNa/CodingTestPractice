import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))

total = [0]*(n+1)
for k in range(n):
	total[k+1] = total[k] + num[k]

for _ in range(m):
    i, j = map(int, input().split())  
    print(total[j] - total[i-1])