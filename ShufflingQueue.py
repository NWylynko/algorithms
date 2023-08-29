from LinkedList import DSALinkedList

# a standard queue
# like people at a food stand
# first in, first out
# we don't bother with resizing the queue
# we just throw an error if it's full


class DSAShufflingQueue():
    def __init__(self, debug: bool = False):
        self._queue = DSALinkedList()
        self._count = 0
        self._debug = debug

    def enqueue(self, value):
        # add a new item to the end of the queue

        if self._debug:
            print("enqueue: ", value)

        self._queue.insertLast(value)
        self._count += 1

    def add(self, value):
        self.enqueue(value)

    def insert(self, value):
        self.enqueue(value)

    def dequeue(self):
        # take the first item from the queue

        if self._debug:
            print("dequeue: ", self._queue.peekFirst())

        if self.isEmpty():
            raise IndexError("Queue is empty")

        value = self._queue.removeFirst()
        self._count -= 1
        return value

    def remove(self):
        return self.dequeue()

    def delete(self):
        return self.dequeue()

    def peek(self):
        # look at the first item, but leave it in the queue

        if self._debug:
            print("peek: ", self._queue.peekFirst())

        if self.isEmpty():
            raise IndexError("Queue is empty")

        return self._queue.peekFirst()

    def front(self):
        return self.peek()

    def isEmpty(self):
        # check if the queue is empty

        if self._debug:
            print("isEmpty: ", self._count == 0)

        return self._count == 0

    def count(self):
        # number of elements in the queue

        if self._debug:
            print("count: ", self._count)

        return self._count


# test the shuffling queue
if __name__ == "__main__":
    queue = DSAShufflingQueue()
    assert queue.isEmpty() == True
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.count() == 3
    assert queue.isEmpty() == False
    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    assert queue.dequeue() == 3
    assert queue.isEmpty() == True
    print("Queue test passed")
