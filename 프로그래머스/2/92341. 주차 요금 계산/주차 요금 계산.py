import math

def solution(fees, records):
    # 요금 기준 4개
    base_time, base_fee, unit_time, unit_fee = fees
    
    parking = {}      # 현재 주차장에 있는 차
    total_time = {}   # 차량별 총 누적 주차 시간
    
    # 입/출차 기록
    for record in records:
        time, car, status = record.split()
        
        # 분 단위로 다 변환시키기
        h, m = map(int, time.split(':'))
        minutes = h * 60 + m
        
        if status == "IN":
            parking[car] = minutes  # 입차시간 기록
            
        elif status == "OUT":
            in_time = parking.pop(car)
            # 현재 - 들어온 시각
            total_time[car] = total_time.get(car, 0) + (minutes - in_time)
            
    # 마감 시간까지 안 나간 차들
    for car, in_time in parking.items():
        # 1439분 - 들어온 시각
        total_time[car] = total_time.get(car, 0) + (1439 - in_time)
        
    # 차량 번호 오름차순 정렬
    # 전체 차량 목록
    sorted_cars = sorted(total_time.keys())
    
    answer = []
    # 정렬된 순서대로 최종 요금 계산
    for car in sorted_cars:
        t = total_time[car] # 이 차의 총 주차 시간
        
        if t <= base_time:
            fee = base_fee
        else:
            # 초과 시간 계산 (총 주차 시간-기본 시간)
            fee = base_fee + math.ceil((t - base_time) / unit_time) * unit_fee
            
        answer.append(fee)
        
    return answer