from itertools import accumulate

from atcoder.atcoder_test import def_input, input

input_text = """
7 1 1 1
1 1 1 1 1 1 1
"""

def_input(input_text)

if __name__ == "__main__":
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))

    accum = [0]
    for idx, val in enumerate(A):
        accum.append(accum[idx] + val)

    set_accum = set(accum)

    for sx in accum:
        sy = P + sx
        sz = Q + sy
        sw = R + sz
        if sy in set_accum and sz in set_accum and sw in set_accum:
            print("Yes")
            exit()
    print("No")
