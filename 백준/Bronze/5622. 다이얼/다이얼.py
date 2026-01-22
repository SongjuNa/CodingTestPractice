s = input()
dial = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

total = 0

for ch in s:
    for i in range(len(dial)):
        if ch in dial[i]:
            total += i + 3

print(total)