from atcoder.atcoder_test import def_input, input

input_text = """
2 10
"""

def_input(input_text)

import itertools

if __name__ == "__main__":
    n, m = map(int, input().split())

    for ptn in itertools.combinations(range(1, m + 1), n):
        print(*ptn)
