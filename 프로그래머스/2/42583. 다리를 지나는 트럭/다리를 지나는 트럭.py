def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    # 다리를 무게0인 트럭들로 초기화
    bridge = [0] * bridge_length
    
    current_weight = 0
    
    # 트럭이 다 지나갈 때까지 반복
    while len(truck_weights) > 0:
        answer += 1
        
        # 현재 다리 맨 앞 트럭이 도착하는 계산
        current_weight -= bridge.pop(0)
        
        # 다음 트럭 올라갈 수 있는지 확인
        if current_weight + truck_weights[0] <= weight:
            new_truck = truck_weights.pop(0)
            bridge.append(new_truck)
            current_weight += new_truck
        else:
            # 다음 트럭 못올라가면 무게 0 주고 시간 늘려야 함
            bridge.append(0)
    
    answer += bridge_length
    return answer