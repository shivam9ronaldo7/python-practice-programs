class UncountableError(ValueError):
    """
    Custom Exception class with ValueError as its super class
    """

    def __init__(self, wrong_value):
        super().__init__(f'Invalid value for n, {wrong_value}. n must be greater that 0')


def count_from_zero_to_n(n):
    if n < 0:
        raise UncountableError(n)

    for x in range(0, n + 1):
        print(x)


value = int(input("Please enter any value: "))

count_from_zero_to_n(value)
