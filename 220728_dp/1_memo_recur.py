from atcoder.atcoder_test import def_input, input

input_text = """
4
10 30 40 20
"""

def_input(input_text)

import sys

sys.setrecursionlimit(10 ** 6)


def rec(i, dp, h):
    if dp[i] != -1:
        return dp[i]

    if i == 0:
        return 0

    if i == 1:
        return abs(h[1] - h[0])

    ret = min(
        rec(i - 1, dp, h) + abs(h[i] - h[i - 1]),
        rec(i - 2, dp, h) + abs(h[i] - h[i - 2]),
    )

    dp[i] = ret

    return ret


if __name__ == "__main__":
    n = int(input())
    h = list(map(int, input().split()))

    # メモ化再帰、DP
    dp = [-1] * n

    print(rec(n - 1, dp, h))
