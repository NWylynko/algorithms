from typing import Union


class DSAListNode:
    def __init__(self, inValue: object):
        self.value = inValue
        self.next: Union[DSAListNode, None] = None
        self.prev: Union[DSAListNode, None] = None


class DSALinkedList:
    def __init__(self):
        self.head: Union[DSAListNode, None] = None
        self.tail: Union[DSAListNode, None] = None

    def isEmpty(self):
        return self.head is None

    def insertFirst(self, value):
        # Insert a new item into the list
        newNode = DSAListNode(value)
        if self.isEmpty():
            self.tail = newNode
        else:
            if self.head is None:
                raise ValueError("Head is None")
            newNode.next = self.head
            self.head.prev = newNode
        self.head = newNode

    def insertLast(self, value):
        # Insert a new item into the list
        newNode = DSAListNode(value)
        if self.isEmpty():
            self.head = newNode
        else:
            if self.tail is None:
                raise ValueError("Tail is None")
            newNode.prev = self.tail
            self.tail.next = newNode
        self.tail = newNode

    def removeFirst(self):
        # Delete an item from the list
        if self.isEmpty():
            raise IndexError("List is empty")
        else:
            if self.head is None:
                raise ValueError("Head is None")
            value = self.head.value
            if self.head.next is None:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
            return value

    def removeLast(self):
        # Delete an item from the list
        if self.isEmpty():
            raise IndexError("List is empty")
        else:
            if self.tail is None:
                raise ValueError("Tail is None")
            value = self.tail.value
            if self.tail.prev is None:
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None
            return value

    def peekFirst(self):
        # Return the data value of an item in the list
        if self.isEmpty():
            raise IndexError("List is empty")
        elif self.head is None:
            raise ValueError("Head is None")
        return self.head.value

    def peekLast(self):
        # Return the data value of an item in the list
        if self.isEmpty():
            raise IndexError("List is empty")
        elif self.tail is None:
            raise ValueError("Tail is None")
        return self.tail.value

    def findNode(self, value):
        # Search for a node with a given data value
        currNode = self.head
        found = False
        while currNode is not None and not found:
            if currNode.value == value:
                found = True
            else:
                currNode = currNode.next
        return currNode

    def find(self, value):
        # Search whether a given data value exists in the list
        currNode = self.head
        found = False
        while currNode is not None and not found:
            if currNode.value == value:
                found = True
            else:
                currNode = currNode.next
        return found

    def toString(self):
        # Return a string representation of the list
        currNode = self.head
        outString = ""
        while currNode is not None:
            outString += str(currNode.value) + ", "
            currNode = currNode.next
        outString = outString[:-2]
        return "[" + outString + "]"

def tests():
    print("Testing DSALinkedList")

    myList = DSALinkedList()

    assert myList.isEmpty() == True, "List should be empty"
    myList.insertLast(1)
    print(myList.toString())
    assert myList.isEmpty() == False, "List should not be empty"
    assert myList.peekFirst() == 1, "Head should be 1"
    assert myList.peekLast() == 1, "Tail should be 1"
    myList.insertLast(2)
    print(myList.toString())
    assert myList.peekFirst() == 1, "Head should be 1"
    assert myList.peekLast() == 2, "Tail should be 2"
    myList.insertLast(3)
    print(myList.toString())
    assert myList.peekFirst() == 1, "Head should be 1"
    assert myList.peekLast() == 3, "Tail should be 3"
    myList.insertFirst(0)
    print(myList.toString())
    assert myList.peekFirst() == 0, "Head should be 0"
    assert myList.peekLast() == 3, "Tail should be 3"
    myList.removeFirst()
    print(myList.toString())
    assert myList.peekFirst() == 1, "Head should be 1"
    assert myList.peekLast() == 3, "Tail should be 3"
    myList.removeLast()
    print(myList.toString())
    assert myList.peekFirst() == 1, "Head should be 1"
    assert myList.peekLast() == 2, "Tail should be 2"
    myList.removeLast()
    print(myList.toString())
    assert myList.peekFirst() == 1, "Head should be 1"
    assert myList.peekLast() == 1, "Tail should be 1"
    myList.removeLast()
    print(myList.toString())
    assert myList.isEmpty() == True, "List should be empty"
    myList.insertLast(1)
    print(myList.toString())
    myList.insertLast(2)
    print(myList.toString())
    myList.insertLast(3)
    print(myList.toString())
    assert myList.find(1) == True, "List should contain 1"
    assert myList.find(2) == True, "List should contain 2"
    assert myList.find(3) == True, "List should contain 3"
    assert myList.find(4) == False, "List should not contain 4"
    myList.removeFirst()
    print(myList.toString())
    myList.insertLast(4)
    print(myList.toString())


    print("All tests passed")

if __name__ == "__main__":
    tests()
