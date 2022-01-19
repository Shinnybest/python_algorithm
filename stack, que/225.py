import collections

class MyStack:
    def __init__(self):
        self.q = collections.deque()

    def push(self, x):
        self.q.append(x)
        # 추가
        for _ in range(len(self.q)-1):
            self.q.append(self.q.popleft())
        print(self.q)


    def pop(self):
        # return self.q.pop()
        return self.q.popleft()

    def top(self):
        # first = self.q.popleft()
        # return first
        return self.q[0]

    def empty(self):
        return len(self.q) == 0

stack = MyStack()
stack.push(1)
stack.push(2)
stack.pop()
print(stack.top())
print(stack)