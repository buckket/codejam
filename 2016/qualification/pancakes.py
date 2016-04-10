#!/usr/bin/env python3


def from_string(string):
    return list(map(lambda x: True if x == "+" else False, string[::-1]))


def do_flip(stack, count=0):
    if all(stack):
        return count
    flip = []
    cseq = stack[-1:]
    while stack[-1:] == cseq:
        flip.append(stack.pop())
    flip = map(lambda x: not x, flip)
    stack.extend(flip)
    return do_flip(stack, count+1)


if __name__ == '__main__':
    t = int(input())
    for i in range(1, t + 1):
        print("Case #{0}: {1}".format(i, do_flip(from_string(input().rstrip()))))
