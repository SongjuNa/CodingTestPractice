# 완전 탐색 문제 - 데이터 개수 100만 개 이하

n = int(input())

count = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1
                
print(count)