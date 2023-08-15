from timeit import timeit


def numberConversion(n: int, toBase: int):
    assert isinstance(n, int) and isinstance(toBase, int), "Both n and toBase must be integers"
    assert n >= 0 and toBase >= 2, "n must be non-negative and toBase must be at least 2"

    if n == 0:
        return 0
    else:
        return n % toBase + 10 * numberConversion(n // toBase, toBase)

def test():
    print("Each test is the sum of 10,000 runs in seconds")

    print("Number Conversion for n 5 to base 2: ", timeit(lambda: numberConversion(5, 2), number=10_000))
    print("Number Conversion for n 5 to base 4: ", timeit(lambda: numberConversion(5, 4), number=10_000))
    print("Number Conversion for n 5 to base 6: ", timeit(lambda: numberConversion(5, 6), number=10_000))

    print("Number Conversion for n 50 to base 2: ", timeit(lambda: numberConversion(50, 2), number=10_000))
    print("Number Conversion for n 50 to base 4: ", timeit(lambda: numberConversion(50, 4), number=10_000))
    print("Number Conversion for n 50 to base 6: ", timeit(lambda: numberConversion(50, 6), number=10_000))

    print("Number Conversion for n 500 to base 2: ", timeit(lambda: numberConversion(500, 2), number=10_000))
    print("Number Conversion for n 500 to base 4: ", timeit(lambda: numberConversion(500, 4), number=10_000))
    print("Number Conversion for n 500 to base 6: ", timeit(lambda: numberConversion(500, 6), number=10_000))

def main():
    
    try:
        number = int(input("Enter a number: "))
        base = int(input("Enter a base: "))

        print("Number Conversion: ", numberConversion(number, base))
        print("Number Conversion seconds (sum of 10,000 runs): ", timeit(lambda: numberConversion(number, base), number=10_000))

    except ValueError:
        print("Please enter a valid number")



if __name__ == '__main__':
    main()
