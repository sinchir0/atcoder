from atcoder.atcoder_test import def_input, input

input_text = """
7
218 786 704 233 645 728 389
"""

def_input(input_text)

import numpy as np
from numba import njit


@njit
def cnt_triangle(A: list, N: int) -> int:
    cnt = 0
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                cnt += A[k] < A[i] + A[j]
    return cnt

if __name__ == "__main__":
    N = int(input())
    A = np.int32(input().split())

    A.sort()

    cnt = cnt_triangle(A, N)
    print(cnt)


