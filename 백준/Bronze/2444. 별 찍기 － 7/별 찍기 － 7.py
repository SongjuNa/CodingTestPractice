n = int(input())

for i in range(2*n - 1):
    if i < n:
        space = n - 1 - i
        star = 2*i + 1
    else:
        space = i - (n - 1)
        star = 2*(2*n - 2 - i) + 1
    print(" " * space + "*" * star)
