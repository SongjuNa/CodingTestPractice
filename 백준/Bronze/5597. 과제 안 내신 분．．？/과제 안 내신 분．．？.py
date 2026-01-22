student = list(range(1, 30+1))
for _ in range(28):
    n = int(input())
    student.remove(n)

student.sort()
for s in student:
    print(s)