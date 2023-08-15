from factorial import test as factorial_test
from fibonacci import test as fibonacci_test
from greatest_common_denominator import test as gcd_test
from number_conversions import test as number_conversions_test
from towers_of_hanoi import test as towers_of_hanoi_test

def test_all():
    print("\nRunning tests...")

    print("\nRunning factorial tests...")
    factorial_test()

    print("\nRunning fibonacci tests...")
    fibonacci_test()

    print("\nRunning gcd tests...")
    gcd_test()

    print("\nRunning number conversions tests...")
    number_conversions_test()

    print("\nRunning towers of hanoi tests...")
    towers_of_hanoi_test()

    print("\nAll tests passed!")

if __name__ == "__main__":
    test_all()