import numpy as np


class DSACircularQueue():
    def __init__(self, maxSize: int = 1000, debug: bool = False):
        self._queue = np.empty(maxSize, dtype=object)
        self._maxSize = maxSize
        self._front = 0
        self._count = 0
        self._rear = 0
        self._debug = debug

    def enqueue(self, value):
        # add a new item to the end of the queue

        if self._debug:
            print("enqueue: ", value, " at ", self._rear)

        if self.isFull():
            raise IndexError("Queue is full")

        self._queue[self._rear] = value
        self._rear = (self._rear + 1) % self._maxSize
        self._count += 1

    def add(self, value):
        self.enqueue(value)

    def insert(self, value):
        self.enqueue(value)

    def dequeue(self):
        # take the first item from the queue

        if self._debug:
            print("dequeue: ", self._queue[self._front], " at ", self._front)

        if self.isEmpty():
            raise IndexError("Queue is empty")

        value = self._queue[self._front]
        self._front = (self._front + 1) % self._maxSize
        self._count -= 1
        return value

    def remove(self):
        return self.dequeue()

    def delete(self):
        return self.dequeue()

    def peek(self):
        # look at the first item, but leave it in the queue

        if self._debug:
            print("peek: ", self._queue[self._front])

        if self.isEmpty():
            raise IndexError("Queue is empty")

        return self._queue[self._front]

    def front(self):
        return self.peek()

    def isEmpty(self):
        # check if the queue is empty

        if self._debug:
            print("isEmpty: ", self._count == 0)

        return self._count == 0

    def isFull(self):
        # check if the queue is full

        if self._debug:
            print("isFull: ", self._count == self._maxSize)

        return self._count == self._maxSize

    def count(self):
        # number of elements in the queue

        if self._debug:
            print("count: ", self._count)

        return self._count


# test the shuffling queue
if __name__ == "__main__":
    queue = DSACircularQueue(5)
    assert queue.isEmpty() == True
    assert queue.isFull() == False
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.count() == 3
    assert queue.isFull() == False
    assert queue.isEmpty() == False
    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    assert queue.dequeue() == 3
    assert queue.isEmpty() == True
    assert queue.isFull() == False
    print("Queue test passed")
