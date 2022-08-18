from atcoder.atcoder_test import def_input, input

input_text = """
2
-3 6
4 2
"""

def_input(input_text)

import numpy as np

if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = 0

    ans = np.dot(A, B)

    if ans == 0:
        print("Yes")
    else:
        print("No")
