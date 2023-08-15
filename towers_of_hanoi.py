from timeit import timeit


def towers_of_hanoi(number: int, source: int, destination: int, recLev: int = 0):
    assert isinstance(number, int) and isinstance(source, int) and isinstance(
        destination, int), "number, source, and destination must be integers"
    assert number >= 1, "number must be greater than or equal to 1"
    assert source != destination, "source and destination must be different"

    recLev += 1

    if number == 1:
        moveDisk(number, source, destination, recLev)
        return 1

    else:
        tmp = 6 - source - destination
        moveDisk(number, source, destination, recLev)
        return towers_of_hanoi(number - 1, source, tmp, recLev) + 1 + towers_of_hanoi(number - 1, tmp, destination, recLev)


def moveDisk(number: int, source: int, destination: int, recLev: int):
    assert isinstance(number, int) and isinstance(source, int) and isinstance(
        destination, int), "number, source, and destination must be integers"

    tabs = "\t" * recLev

    print(tabs + "Recursion Level=" + str(recLev))
    print(tabs + "Moving Disk", number, "from Source",
          source, "to Destination", destination)
    print(tabs + "n=" + str(number) + ", src=" +
          str(source) + ", dest=" + str(destination))


def test():
    print("Towers of Hanoi for number 3, source 1, destination 3: ",
          timeit(lambda: towers_of_hanoi(3, 1, 3), number=1))


def main():

    try:
        number = int(input("Enter a number: "))
        source = int(input("Enter a source: "))
        destination = int(input("Enter a destination: "))

        print("seconds to run Towers of Hanoi", timeit(lambda: print(
            "Moves required:", towers_of_hanoi(number, source, destination)), number=1))

    except ValueError:
        print("Please enter a valid number")


if __name__ == '__main__':
    main()
