import numpy as np


class DSAStack():
    def __init__(self, maxSize: int = 1000, debug: bool = False):
        self._stack = np.empty(maxSize, dtype=object)
        self._maxSize = maxSize
        self._count = 0
        self._debug = debug

    def push(self, value):
        # add a new item to the top of the stack

        if self.isFull():
            raise IndexError("Stack is full")

        self._stack[self._count] = value
        self._count += 1

    def pop(self):
        # take the top-most item from the stack

        if self.isEmpty():
            raise IndexError("Stack is empty")

        self._count -= 1
        return self._stack[self._count]

    def top(self):
        # look at the top-most item, but leave it on the stack

        if self.isEmpty():
            raise IndexError("Stack is empty")

        return self._stack[self._count - 1]

    def peek(self):
        return self.top()

    def isEmpty(self):
        # check if the stack is empty

        if self._debug:
            print("isEmpty: ", self._count == 0)

        return self._count == 0

    def count(self):
        # checks if the stack is full

        if self._debug:
            print("count: ", self._count)

        return self._count

    def isFull(self):
        # number of elements in the stack

        if self._debug:
            print("isFull: ", self.count() == self._maxSize)

        return self.count() == self._maxSize


# test the stack
if __name__ == "__main__":
    stack = DSAStack(5, True)
    assert stack.isEmpty() == True
    assert stack.isFull() == False
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.count() == 3
    assert stack.isFull() == False
    assert stack.isEmpty() == False
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.isEmpty() == True
    assert stack.isFull() == False
    print("Stack test passed")

    # test: Application: Palindrome
    palindrome = "racecar"
    stack = DSAStack(len(palindrome))
    for letter in palindrome:
        stack.push(letter)
    reverse = ""
    while not stack.isEmpty():
        reverse += stack.pop()
    assert reverse == palindrome
    print("Palindrome test passed")
