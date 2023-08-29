from LinkedList import DSALinkedList


class DSAStack():
    def __init__(self, debug: bool = False):
        self._stack = DSALinkedList()
        self._count = 0
        self._debug = debug

    def push(self, value):
        # add a new item to the top of the stack

        self._stack.insertFirst(value)
        self._count += 1

    def pop(self):
        # take the top-most item from the stack

        if self.isEmpty():
            raise IndexError("Stack is empty")

        self._count -= 1
        return self._stack.removeFirst()

    def top(self):
        # look at the top-most item, but leave it on the stack

        if self.isEmpty():
            raise IndexError("Stack is empty")

        return self._stack.peekFirst()

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


# test the stack
if __name__ == "__main__":
    stack = DSAStack(True)
    assert stack.isEmpty() == True
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.count() == 3
    assert stack.isEmpty() == False
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.isEmpty() == True
    print("Stack test passed")

    # test: Application: Palindrome
    palindrome = "racecar"
    stack = DSAStack()
    for letter in palindrome:
        stack.push(letter)
    reverse = ""
    while not stack.isEmpty():
        reverse += stack.pop()
    assert reverse == palindrome
    print("Palindrome test passed")
