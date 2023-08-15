from timeit import timeit


def greatest_common_denominator(num1: int, num2: int):
    assert isinstance(num1, int) and isinstance(num2, int), "Both num1 and num2 must be integers"
    assert num1 >= 0 and num2 >= 0, "Both num1 and num2 must be non-negative"

    if num1 == 0:
        return num2
    elif num2 == 0:
        return num1
    elif num1 == num2:
        return num1
    elif num1 > num2:
        return greatest_common_denominator(num1 - num2, num2)
    else:
        return greatest_common_denominator(num1, num2 - num1)


def test():
    print("Each test is the sum of 10,000 runs in seconds")

    print("GCD for num1 5 and num2 10: ", timeit(lambda: greatest_common_denominator(5, 10), number=10_000))
    print("GCD for num1 5 and num2 15: ", timeit(lambda: greatest_common_denominator(5, 15), number=10_000))
    print("GCD for num1 5 and num2 25: ", timeit(lambda: greatest_common_denominator(5, 25), number=10_000))

    print("GCD for num1 6 and num2 12: ", timeit(lambda: greatest_common_denominator(6, 12), number=10_000))
    print("GCD for num1 6 and num2 18: ", timeit(lambda: greatest_common_denominator(6, 18), number=10_000))
    print("GCD for num1 6 and num2 24: ", timeit(lambda: greatest_common_denominator(6, 24), number=10_000))

    print("GCD for num1 7 and num2 14: ", timeit(lambda: greatest_common_denominator(7, 14), number=10_000))
    print("GCD for num1 7 and num2 21: ", timeit(lambda: greatest_common_denominator(7, 21), number=10_000))
    print("GCD for num1 7 and num2 28: ", timeit(lambda: greatest_common_denominator(7, 28), number=10_000))

def main():
    
    try:
        num1 = int(input("Enter a num1: "))
        num2 = int(input("Enter a num2: "))

        print("GCD: ", greatest_common_denominator(num1, num2))
        print("GCD seconds (sum of 10,000 runs): ", timeit(lambda: greatest_common_denominator(num1, num2), number=10_000))

    except ValueError:
        print("Please enter a valid number")



if __name__ == '__main__':
    main()
