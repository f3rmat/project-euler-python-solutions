"""Solution for problem 1 of Project Euler."""

import time


def solve(limit: int) -> int:
    """Calculates the sum of all numbers below 1000 which are multiples of 3 or 5."""
    ans = 0
    for i in range(1, limit):
        if i % 3 == 0 or i % 5 == 0:
            ans = ans + i
    return ans


if __name__ == "__main__":
    start = time.time()
    print("Answer is: ", solve(1000))
    end = time.time()
    print("Time taken: ", (end - start) * 1000, " milliseconds.")
