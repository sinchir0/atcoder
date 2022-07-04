# https://atcoder.jp/contests/abc258/submissions/32947228

from atcoder.atcoder_test import def_input, input

input_text = """
4
9899
8711
8171
8116
"""

def_input(input_text)

if __name__ == "__main__":

    dydx8 = ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1))

    n = int(input())
    board = [list(map(int, input())) for _ in range(n)]

    ans = 0

    # 盤面の全ての位置から、8方向に対して数値の計算を行い、全探索する
    # 高々, 1 ≤ N ≤ 10, のため、もし8方向に全探索を行っても、10 * 10 * 8 = 800程度であり問題ないことが分かる
    for i in range(n):
        for j in range(n):
            for dy, dx in dydx8:
                x, y = i, j
                tmp = board[i][j]

                # (dy, dx)へN回移動する
                for _ in range(n - 1):
                    x += dx
                    y += dy
                    x %= n
                    y %= n
                    tmp = 10 * tmp + board[x][y]

                # 現在のansとtmpで計算した数値の大きい方を採用する
                ans = max(ans, tmp)

    print(ans)
