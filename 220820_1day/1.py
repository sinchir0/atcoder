from atcoder.atcoder_test import def_input, input

input_text = """
6 5 4
3
1
3
2
"""

def_input(input_text)

import collections

if __name__ == "__main__":
    N, K, Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]

    c = collections.Counter(A)

    for i in range(N):
        if Q - c[i+1] >= K:
            print("No")
        else:
            print("Yes")
