from atcoder.atcoder_test import def_input, input

input_text = """
"""

def_input(input_text)

if __name__ == "__main__":
    n = int(input())
    h = list(map(int, input().split()))

    # 配るDP

    INF = 1 << 60
    dp = [INF] * n  # dp[i] := i番目の足場に来るときの最小コスト
    dp[0] = 0

    for i in range(n):
        if i + 1 < n:  # 配列外参照を防ぐ
            dp[i + 1] = min(dp[i + 1], dp[i] + abs(h[i] - h[i + 1]))

        if i + 2 < n:  # 配列外参照を防ぐ
            dp[i + 2] = min(dp[i + 2], dp[i] + abs(h[i] - h[i + 2]))

    print(dp[n - 1])
