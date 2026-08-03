from collections import deque
class MyStack:

    def __init__(self):  #def __init__(): 생성자, self: 생성된 객체
        self.queue = deque()
        self.temp_queue = deque()
        
    def push(self, x: int) -> None:
        #새로운 데이터는 temp_queue에 삽입
        self.temp_queue.append(x)
        #기존에 있던 데이터 모두 temp_queue로 이동
        while self.queue:
            self.temp_queue.append(self.queue.popleft())
        #임시 큐, 실제 큐 바꿔치기
        self.queue, self.temp_queue = self.temp_queue, self.queue

    #앞의 값 빼기
    def pop(self) -> int:
        return self.queue.popleft()

    #제일 앞의 값 확인
    def top(self) -> int:
        return self.queue[0]

    #비어있는지 확인    
    def empty(self) -> bool:
        return len(self.queue) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()