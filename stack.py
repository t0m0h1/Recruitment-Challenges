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
    while True:
        url = input("Enter a URL (or 'exit' to quit): ")
        if url == 'exit':
            break
        stack.pushtostack(url)
    
    print("Browser History:")
    while not stack.is_empty():
        print(stack.popfromstack())
