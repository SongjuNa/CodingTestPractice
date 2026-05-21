n = int(input())

array = []
for _ in range(n):
    student_inform = input().split()
    array.append((student_inform[0], int(student_inform[1])))

array = sorted(array, key=lambda student: student[1])

for student in array:
    print(student[0], end=' ')