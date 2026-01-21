a, b = map(int, input().split())
c = int(input())

total = b + c

if total < 60:
    print(a, total)
else:
    a = (a + total // 60) % 24
    b = total % 60
    print(a, b)
