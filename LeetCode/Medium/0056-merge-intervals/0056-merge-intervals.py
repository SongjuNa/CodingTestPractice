class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        output = []
        intervals.sort()

        for curr in intervals:
            # 스택이 비어있거나 구간이 안 겹칠 때
            if not output or output[-1][1] < curr[0]:
                output.append(curr)
                
            # 구간 겹칠 때
            else:
                output[-1][1] = max(output[-1][1], curr[1])
            
        return output