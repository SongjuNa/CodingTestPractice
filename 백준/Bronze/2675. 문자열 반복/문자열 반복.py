t = int(input())

for _ in range(t):
    r, s = input().split()
    
    p = ""
    for i in s:
        p += i*int(r)
    print(p)