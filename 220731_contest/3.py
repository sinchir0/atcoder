from atcoder.atcoder_test import def_input, input

input_text = """
4
1 3 2 4
"""

def_input(input_text)

import itertools
from collections import defaultdict

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))

    d = defaultdict(int)
    for idx, val in enumerate(a):
        d[idx] = val
    
    d = sorted(d.items(), key=lambda x: x[1])

    for i, j in d:
        if i + 1 == j:

