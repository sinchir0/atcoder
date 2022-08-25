from itertools import accumulate

from atcoder.atcoder_test import def_input, input

input_text = """
10 5 7 5
1 3 2 2 2 3 1 4 3 2
"""

def_input(input_text)

from bisect import bisect_left

if __name__ == "__main__":
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))

    S = [0]
    for idx, val in enumerate(A):
        S.append(S[idx] + val)

    # bisect_leftで一番右側のidx(rft_idx)が取れた場合、S[rft_idx]がIndexErrorになってしまうため
    S.append(float("inf"))

    for x in range(N - 1):
        y = bisect_left(S, P + S[x])
        if S[y] - S[x] != P:
            continue

        z = bisect_left(S, Q + S[y])
        if S[z] - S[y] != Q:
            continue

        w = bisect_left(S, R + S[z])
        if S[w] - S[z] != R:
            continue

        print("Yes")
        exit()

    print("No")
