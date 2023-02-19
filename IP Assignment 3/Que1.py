def print_upper_half(n, row):
    if n <= 0:
        return

    spaces = 2 * row
    print("*" * n + " " * spaces + "*" * n)
    return print_upper_half(n-1, row+1)


def print_lower_half(n, row):
    if row <= -1:
        return

    spaces = 2 * row
    print("*" * n + " " * spaces + "*" * n)
    return print_lower_half(n+1, row-1)


try:
    n = int(input('Enter the value of n: '))
    if n <= 0:
        raise ValueError
except ValueError:
    print("Invalid input. 'n' must be a positive integer.")
else:
    print_upper_half(n, 0)
    print_lower_half(2, n-2)
