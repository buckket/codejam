#!/usr/bin/env python3


def count_number(starting_number):
    if starting_number == 0:
        return "INSOMNIA"

    digits = set()
    counting_number = 0
    # Instead of a while loop, a for x in range() loop could have saved
    # me from using counting_number the way I did. Replace counting_number:
    # counting_number = starting_number * x, and add break check at the end.
    while len(digits) != 10:
        counting_number += starting_number
        # Could have just iterated over str(counting_number),
        # casting to int() later would have been optional.
        for digit in [int(i) for i in str(counting_number)]:
            digits.add(digit)
    return counting_number


if __name__ == '__main__':
    t = int(input())
    for i in range(1, t + 1):
        print("Case #{0}: {1}".format(i, count_number(int(input()))))
