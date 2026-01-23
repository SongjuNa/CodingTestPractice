# 과목평점
avg = {"A+": 4.5, "A0": 4.0, "B+": 3.5, 
       "B0": 3.0, "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0}

total = 0.0  # score*avg 합
total_score = 0.0 # P 제외 학점 합

# 과목명, 학점, 등급
for _ in range(20):
    obj, score, grade = input().split()
    score = float(score)
    
    if grade == "P":
        continue
    total += score * avg[grade]
    total_score += score

print(total / total_score)