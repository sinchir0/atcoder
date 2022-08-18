from atcoder.atcoder_test import def_input, input

input_text = """
200
"""

def_input(input_text)

import math


def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


if __name__ == "__main__":
    L = int(input())
    print(combinations_count(L - 1, 11))
