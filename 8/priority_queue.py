from heap import Heap

class PriorityQueue:
    def __init__(self):
        self.heap = Heap(is_min=True)

    def enqueue(self, item, priority):
        self.heap.insert((priority, item))

    def dequeue(self):
        if self.heap.peek() is None:
            return None
        # извлекаем кортеж (priority, item) и возвращаем только item
        _, item = self.heap.extract()
        return item

    def peek(self):
        if self.heap.peek() is None:
            return None
        return self.heap.peek()[1]  # возвращаем только item
