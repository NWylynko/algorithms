import numpy as np

# a standard queue
# like people at a food stand
# first in, first out
# we don't bother with resizing the queue
# we just throw an error if it's full


class DSAShufflingQueue():
    def __init__(self, maxSize: int = 1000, debug: bool = False):
        self._queue = np.empty(maxSize, dtype=object)
        self._maxSize = maxSize
        self._count = 0
        self._debug = debug

    def enqueue(self, value):
        # add a new item to the end of the queue

        if self._debug:
            print("enqueue: ", value)

        if self.isFull():
            raise IndexError("Queue is full")

        self._queue[self._count] = value
        self._count += 1

    def add(self, value):
        self.enqueue(value)

    def insert(self, value):
        self.enqueue(value)

    def dequeue(self):
        # take the first item from the queue

        if self._debug:
            print("dequeue: ", self._queue[0])

        if self.isEmpty():
            raise IndexError("Queue is empty")

        value = self._queue[0]
        for i in range(1, self._count):
            self._queue[i - 1] = self._queue[i]
        self._count -= 1
        return value

    def remove(self):
        return self.dequeue()

    def delete(self):
        return self.dequeue()

    def peek(self):
        # look at the first item, but leave it in the queue

        if self._debug:
            print("peek: ", self._queue[0])

        if self.isEmpty():
            raise IndexError("Queue is empty")

        return self._queue[0]

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
    queue = DSAShufflingQueue(5)
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
