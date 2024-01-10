class Queue:
    """Queue implementation as a list"""
    '''A queue is a data structure that follows the FIFO (First In First Out) principle.'''
    '''The first element added to the queue will be the first one to be removed.'''

    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    print(q.size())  