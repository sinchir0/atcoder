from atcoder.atcoder_test import def_input, input

input_text = """
"""

def_input(input_text)

if __name__ == "__main__":
    # もらうDP
    n = int(input())
    h = list(map(int, input().split()))

    dp = [0] * n  # dp[i] := i番目の足場に来るときの最小コスト

    # i == 0
    dp[0] = 0
    # i == 1
    dp[1] = abs(h[0] - h[1])

    for i in range(2, n):
        dp[i] = min(dp[i - 1] + abs(h[i - 1] - h[i]), dp[i - 2] + abs(h[i - 2] - h[i]))

    print(dp[n - 1])
