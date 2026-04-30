class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        n = len(intervals)
        
        # 겹치지 않는 부분
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
            
        # 겹치는 부분
        while i < n and intervals[i][0] <= newInterval[1]:
            # newInterval을 업데이트
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        result.append(newInterval)
        
        # 겹치지 않는 뒤의 남은 나머지 구간들
        while i < n:
            result.append(intervals[i])
            i += 1
        
        
        return result