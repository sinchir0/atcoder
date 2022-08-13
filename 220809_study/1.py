from atcoder.atcoder_test import def_input, input

input_text = """
6 3
2 7 1 8 2 8
2 10
3 1
5 5
"""

def_input(input_text)

from collections import defaultdict

if __name__ == "__main__":

    n, m = map(int, input().split())

    x = [0] + list(map(int, input().split()))

    bonus = defaultdict(int)
    for _ in range(m):
        c, y = map(int, input().split())
        bonus[c] = y

    MINUS_INF = -float("inf")

    dp = [MINUS_INF] * 5500

    dp[1] = x[1] + bonus[1]

    # 1回目にT
    dp[0] = 0

    # dpは一つ前の列、nxtは今回調査する列を調べる
    for i in range(1, n):
        nxt = [MINUS_INF] * 5500

        for j in range(n):
            # i, j := i回目にj連続Hが出ている
            if dp[j] == MINUS_INF:
                continue

            # i+1回目はHの場合
            nxt[j + 1] = max(nxt[j + 1], dp[j] + x[i + 1] + bonus[j + 1])

            # i+1回目はT(tail,裏)
            nxt[0] = max(nxt[0], dp[j])

        dp = nxt

    print(max(dp))
