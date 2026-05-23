import sys
# 재귀 한도 업
sys.setrecursionlimit(200000)

def solution(k, room_number):
    rooms = {}
    answer = []
    
    def find_empty_room(num):
        if num not in rooms:
            rooms[num] = num + 1
            return num
        
        empty = find_empty_room(rooms[num])
        
        rooms[num] = empty + 1
        return empty

    for num in room_number:
        empty_room = find_empty_room(num)
        answer.append(empty_room)
        
    return answer