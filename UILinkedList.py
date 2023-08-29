from LinkedList import DSALinkedList

running = True
list = DSALinkedList()

while running:

    print("\nList: ", list.toString())
    print("1. Insert First")
    print("2. Insert Last")
    print("3. Remove First")
    print("4. Remove Last")

    choice = input("Enter choice: ")

    if choice == "1":
        value = input("Enter value: ")
        list.insertFirst(value)

    elif choice == "2":
        value = input("Enter value: ")
        list.insertLast(value)

    elif choice == "3":
        list.removeFirst()

    elif choice == "4":
        list.removeLast()
