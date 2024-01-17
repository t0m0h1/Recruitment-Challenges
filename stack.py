class Stack:
    def __init__(self):
        self.items = []

    def pushtostack(self, item):
        self.items.append(item)
    
    def popfromstack(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        return self.items[-1]
    
    def is_empty(self):
        return len(self.items) == 0
    
    def length(self):
        return len(self.items)


if __name__ == '__main__':
    stack = Stack()
    for i in range(0, 21):
        stack.pushtostack(2)
    print(stack.length())