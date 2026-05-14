class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        output = []
        intervals.sort()

        for curr in intervals:
            # 조건 1: 스택이 비어있거나, 안 겹칠 때 -> 그냥 스택에 넣는다
            if not output or output[-1][1] < curr[0]:
                output.append(curr)
                
            # 조건 2: 겹칠 때 -> 스택 마지막 구간의 '끝나는 시간'을 늘려준다!
            else:
                output[-1][1] = max(output[-1][1], curr[1])
            
        return output