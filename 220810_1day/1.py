from atcoder.atcoder_test import def_input, input

input_text = """
3
1 3 2
3 1 2
"""

def_input(input_text)

import itertools

if __name__ == "__main__":
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))

    cand = list(range(1, N + 1))

    for idx, val in enumerate(itertools.permutations(cand)):
        if P == list(val):
            p_num = idx
        if Q == list(val):
            q_num = idx
    print(abs(p_num - q_num))
