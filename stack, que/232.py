class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x):
        self.input.append(x)
        print(self.input)

    def pop(self):
        self.peek()
        return self.output.pop()


    def peek(self):
        if not self.output and not self.input:
            print("Nothing")
            print(self.output, self.input)
            exit(0)

        if not self.output:
            while self.input:
                self.output.append(self.input.pop())

        print(self.output)
        return self.output[-1]

    def empty(self):
        return not self.input and not self.output

queue = MyQueue()

queue.push(1)
queue.push(2)
queue.pop()
queue.pop()
queue.peek()
print(queue.empty())
