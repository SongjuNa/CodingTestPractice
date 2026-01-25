import sys

max_val = -1
max_r, max_c = 1, 1

for r in range(1, 10):  # 1~9 (행)
    row = list(map(int, sys.stdin.readline().split()))
    for c in range(1, 10):  # 1~9 (열)
        if row[c-1] > max_val:
            max_val = row[c-1]
            max_r, max_c = r, c

print(max_val)
print(max_r, max_c)
