# https://atcoder.jp/contests/abc143/submissions/34309157
from atcoder.atcoder_test import def_input, input

input_text = """
4
3 4 2 1
"""

def_input(input_text)

import bisect

if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))

    A = sorted(A)

    ans = 0
    # a <= b <= cとする
    for i in range(N):
        for j in range(i + 1, N):
            a = A[i]
            b = A[j]

            # a+bより小さい値の数がc_cand_numとなる(c < a+bの条件を満たす数)
            c_cand_num = bisect.bisect_left(A, a + b)

            # c_cand_numから,bまでの数字の個数を引く、jはindexであり、c_cand_numは個数のため、j+1を引く。
            ans += c_cand_num - (j + 1)
    print(ans)
