from timeit import timeit


def fibIterative(n):
    assert isinstance(n, int) and n >= 0, "n must be a non-negative integer"
    
    fibVal = 0
    currVal = 1
    lastVal = 0

    if (n == 0):
        fibVal = 0
    elif (n == 1):
        fibVal = 1
    else:
        for ii in range(2, n+1):
            fibVal = currVal + lastVal
            lastVal = currVal
            currVal = fibVal
    return fibVal


def fibRecursive(n):
    assert isinstance(n, int) and n >= 0, "n must be a non-negative integer"
    
    fibVal = 0

    if (n == 0):
        fibVal = 0
    elif (n == 1):
        fibVal = 1
    else:
        fibVal = fibRecursive(n-1) + fibRecursive(n-2)
    return fibVal


def test():
    print("Each test is the sum of 10,000 runs in seconds")

    print("Iterative Fibonacci for n 5: ", timeit(lambda: fibIterative(5), number=10_000))
    print("Recursive Fibonacci for n 5: ", timeit(lambda: fibRecursive(5), number=10_000))

    print("Iterative Fibonacci for n 10: ", timeit(lambda: fibIterative(10), number=10_000))
    print("Recursive Fibonacci for n 10: ", timeit(lambda: fibRecursive(10), number=10_000))

    print("Iterative Fibonacci for n 15: ", timeit(lambda: fibIterative(15), number=10_000))
    print("Recursive Fibonacci for n 15: ", timeit(lambda: fibRecursive(15), number=10_000))

def main():
    
    try:
        number = int(input("Enter a number: "))

        print("Iterative Fibonacci: ", fibIterative(number))
        print("Recursive Fibonacci: ", fibRecursive(number))

        print("Iterative Fibonacci seconds (sum of 10,000 runs): ", timeit(lambda: fibIterative(number), number=10_000))
        print("Recursive Fibonacci seconds (sum of 10,000 runs): ", timeit(lambda: fibRecursive(number), number=10_000))

    except ValueError:
        print("Please enter a valid number")



if __name__ == '__main__':
    main()
