from timeit import timeit


def calcNFactorial(n):
    assert isinstance(n, int) and n >= 0, "n must be a non-negative integer"
    
    nFactorial = 1
    for ii in range(n, 1, -1):
        nFactorial = nFactorial * ii
    return nFactorial


def calcNFactorialRecursive(n):
    assert isinstance(n, int) and n >= 0, "n must be a non-negative integer"
    
    if (n == 0):
        return 1
    else:
        return n * calcNFactorialRecursive(n-1)


def test():
    print("Each test is the sum of 10,000 runs in seconds")

    print("Iterative Factorial for n 5: ", timeit(lambda: calcNFactorial(5), number=10_000))
    print("Recursive Factorial for n 5: ", timeit(lambda: calcNFactorialRecursive(5), number=10_000))

    print("Iterative Factorial for n 50: ", timeit(lambda: calcNFactorial(50), number=10_000))
    print("Recursive Factorial for n 50: ", timeit(lambda: calcNFactorialRecursive(50), number=10_000))

    print("Iterative Factorial for n 500: ", timeit(lambda: calcNFactorial(500), number=10_000))
    print("Recursive Factorial for n 500: ", timeit(lambda: calcNFactorialRecursive(500), number=10_000))

def main():
    
    try:
        number = int(input("Enter a number: "))

        print("Iterative Factorial: ", calcNFactorial(number))
        print("Recursive Factorial: ", calcNFactorialRecursive(number))

        print("Iterative Factorial seconds (sum of 10,000 runs): ", timeit(lambda: calcNFactorial(number), number=10_000))
        print("Recursive Factorial seconds (sum of 10,000 runs): ", timeit(lambda: calcNFactorialRecursive(number), number=10_000))

    except ValueError:
        print("Please enter a valid number")



if __name__ == '__main__':
    main()
