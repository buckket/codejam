#!/usr/bin/env python3


def count_number(starting_number):
    if starting_number == 0:
        return "INSOMNIA"

    digits = set()
    counting_number = 0
    while len(digits) != 10:
        counting_number += starting_number
        for digit in [int(i) for i in str(counting_number)]:
            digits.add(digit)
    return counting_number


if __name__ == '__main__':
    t = int(input())
    for i in range(1, t + 1):
        print("Case #{0}: {1}".format(i, count_number(int(input()))))
