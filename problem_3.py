"""Solution for problem 3 of Project Euler."""

import time


def solve_approach_2(num: int) -> int:
    """Calculates the largest prime factor of a number."""
    max_value = 1
    while num % 2 == 0:
        max_value = 2
        num //= 2
    while num % 3 == 0:
        max_value = 3
        num //= 3

    # The rest of the prime numbers are of the form 6k +/- 1.
    d = 6
    while num > 1:
        while num % (d - 1) == 0:
            max_value = d - 1
            num //= d - 1
        while num % (d + 1) == 0:
            max_value = d + 1
            num //= d + 1
        d += 6
        if d * d > num:
            max_value = max(max_value, num)
            break

    return max_value


def solve_approach_1(num: int) -> int:
    """Calculates the largest prime factor of a number."""
    max_value = 1
    d = 2
    while num > 1:
        while num % d == 0:
            max_value = max(max_value, d)
            num //= d
        d = d + (1 if d == 2 else 2)
        if d * d > num:
            max_value = max(max_value, num)
            break

    return max_value


if __name__ == "__main__":
    start = time.time()
    print("Answer is: ", solve_approach_2(600_851_475_143))
    end = time.time()
    print("Time taken: ", (end - start) * 1000, " milliseconds.")
