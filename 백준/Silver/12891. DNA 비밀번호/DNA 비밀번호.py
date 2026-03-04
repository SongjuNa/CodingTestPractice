import sys
input = sys.stdin.readline

S, P = map(int, input().split())
dna = input().strip()
min_req = list(map(int, input().split()))  # A C G T 최솟값

# 인덱스 매핑
idx = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
cnt = [0] * 4  # 현재 윈도우 내 4개 문자 개수 저장
satisfied = 0  # 조건 만족하는 알파벳 종류 수
answer = 0

# min_req가 0인 항목 미리 반영
for i in range(4):
    if min_req[i] == 0:
        satisfied += 1

def add(c):
    global satisfied   # 함수 밖에서 선언된 변수를 함수 안에서 수정 -> global변수
    i = idx[c]  # 문자를 숫자로 변환(idx에서 선언된 것대로)
    cnt[i] += 1  # 현재 window의 해당 문자 개수를 1 증가
    if cnt[i] == min_req[i]:  # 딱 충족되는 순간
        satisfied += 1  # 조건 하나 달성

def remove(c):
    global satisfied
    i = idx[c]  # 문자를 숫자로 변환(idx에서 선언된 것대로)
    if cnt[i] == min_req[i]:  # 충족이 깨지는 순간
        satisfied -= 1     # 조건 충족 못함
    cnt[i] -= 1    # 실제 개수 1 감소

# 초기 윈도우 설정
for i in range(P):  # 처음부터 P 길이만큼 문자를 하나씩 add 함수에 넣음
    add(dna[i])

if satisfied == 4:   # 만약 A, C, G, T 4가지 조건을 모두 만족했다면
    answer += 1    # 정답 1 증가

# 슬라이딩
for i in range(P, S):     # i는 새로 들어올 문자의 위치 (P번 인덱스부터 끝까지)
    add(dna[i])     # 새로운 오른쪽 끝 문자 추가
    remove(dna[i - P])   # 가장 왼쪽 끝(현재 i에서 P만큼 떨어진 곳) 문자 제거
    if satisfied == 4:   # 이 상태에서 4가지 조건을 모두 만족하면
        answer += 1    # 정답 증가

print(answer)