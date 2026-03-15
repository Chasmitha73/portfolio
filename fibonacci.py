"""Fibonacci problem examples.

Usage:
  python fibonacci.py          # runs interactive prompt
  python fibonacci.py 10      # prints first 10 Fibonacci numbers
"""

import sys


def fib(n: int) -> int:
    """Return the nth Fibonacci number (0-indexed).

    Args:
        n: non-negative index.

    Returns:
        The nth Fibonacci number.
    """

    if n < 0:
        raise ValueError("n must be non-negative")

    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def fib_sequence(n: int) -> list[int]:
    """Return the first n Fibonacci numbers (starting from 0)."""

    if n < 0:
        raise ValueError("n must be non-negative")
    return [fib(i) for i in range(n)]


def main(argv: list[str] | None = None) -> None:
    if argv is None:
        argv = sys.argv[1:]

    if len(argv) == 0:
        try:
            n = int(input("Enter how many Fibonacci numbers to compute: "))
        except ValueError:
            print("Please enter a valid integer.")
            return
    else:
        try:
            n = int(argv[0])
        except ValueError:
            print("Usage: python fibonacci.py [count]")
            return

    if n < 0:
        print("Count must be non-negative.")
        return

    seq = fib_sequence(n)
    print("Fibonacci:", seq)


if __name__ == "__main__":
    main()
