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

    # 答えの動画
    # 動画: https://www.youtube.com/watch?v=P20UCEOnUzU

    # 個人的なメモ
    # DPには、配る、もらう、メモ化再帰の３種類がある

    n, m = map(int, input().split())
    # [0]を最初に追加することで、0-indexにする
    x = [0] + list(map(int, input().split()))

    bonus = defaultdict(int)
    for _ in range(m):
        c, y = map(int, input().split())
        bonus[c] = y

    MINUS_INF = -float("inf")

    dp = [MINUS_INF] * 5500  # dp[j] := i回目にj連続H(head,表)だった時に持っているコインの最大値

    # 1回目にH
    # bonusは呼ばれても、該当しない場合は0を返す
    dp[1] = x[1] + bonus[1]

    # 1回目にT
    dp[0] = 0

    # dpは一つ前の列、nxtは今回調査する列を調べる

    for i in range(1, n):  # 配るDP: i回目からi+1回目への遷移を考える
        nxt = [MINUS_INF] * 5500

        for j in range(n):
            # i, j := i回目にj連続Hが出ている
            if dp[j] == MINUS_INF:
                continue

            # i+1回目はHの場合
            # maxでnxt[j+1]を行うのは、既にnxt[j+1]に値がある場合を想定している
            # 動画より、maxの候補としては、前回の数字(dp[j])をベースに、今回のxの値(x[i+1])とbonusを足した数字になる
            nxt[j + 1] = max(nxt[j + 1], dp[j] + x[i + 1] + bonus[j + 1])

            # i+1回目はT(tail,裏)
            nxt[0] = max(nxt[0], dp[j])

        dp = nxt

    print(max(dp))
