import sys
input = sys.stdin.readline

n = int(input())
a = []

for i in range(n):
    a.append((int(input()), i)) 
             
max_move = 0
sorted_a = sorted(a) # 정렬된 새로운 a

for j in range(n):
    if max_move < sorted_a[j][1] - j:
        max_move = sorted_a[j][1] - j
        
print(max_move + 1)