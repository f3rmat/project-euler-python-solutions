"""Solution for problem 2 of Project Euler."""

import time


def solve(limit: int) -> int:
    """Calculates the sum of all even valued Fibonacci numbers below 4 million."""
    ans = 0
    a = 1
    b = 2
    while b < limit:
        if b % 2 == 0:
            ans = ans + b
        a, b = b, a + b
    return ans


if __name__ == "__main__":
    start = time.time()
    print("Answer is: ", solve(4_000_000))
    end = time.time()
    print("Time taken: ", (end - start) * 1000, " milliseconds.")
