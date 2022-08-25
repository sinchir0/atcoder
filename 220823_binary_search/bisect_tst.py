from atcoder.atcoder_test import def_input, input

input_text = """
5 5
1 2 3 4 5
6
5
4
3
2
"""

def_input(input_text)

from bisect import bisect_left


def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))

    A = sorted(A)

    res = [0] * Q
    for idx in range(Q):
        x = int(input())

        res[idx] = N - bisect_left(A, x)

    print(*res, sep="\n")


if __name__ == "__main__":
    main()
