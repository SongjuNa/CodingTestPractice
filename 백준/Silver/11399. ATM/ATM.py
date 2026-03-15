n = int(input())
Pi = list(map(int, input().split()))

Pi.sort()
total = 0
current_sum = 0
temp = []
for i in range(n):
    current_sum += Pi[i]
    temp.append(current_sum)
total = sum(temp)
print(total)