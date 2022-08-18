# input

# 数字一つ
a = int(input())

# 数字の列
a, b, c, d = map(int, input().split())

# 数字の列を一つの配列で持つ
N = map(int, list(input()))

# 数字のlist
num_list = list(map(int, input().split()))

# 数字の配列のlist
num_arr_list = [list(map(int, input().split())) for _ in range(n)]

# 盤面のlist
board = [list(input()) for _ in range(r)]

# 12
# 34
# みたいに、間にスペースを挟まない場合
board = [list(map(int, input())) for _ in range(n)]

# 1始まりを0始まりに変換
sy, sx = map(lambda x: int(x) - 1, input().split())


# トーラス型への対応
# 盤面の一番右を更に右に進むと、盤面の一番左に繋がるやつ
x %= n
y %= n


# 定数
ans = 1001001001  # ちょうど10桁と分かりやすく、32bitでもC言語だったらオーバーフローしない数字


# 切り上げ、切り捨て
n // w  # 切り捨て
(n + w - 1) // w  # 切り上げ


# 小数点以下の計算をしないために
# もし100 * 1.08をしたい場合は
100 * 108 // 100

# >>> 100 * 108 // 100
# 108

# >>> 100 * 1.08
# 108.0

# 最小値を求める場合の答えの初期値

INF = float("inf")
MINUS_INF = -float("inf")

# 方向の探索

# 4方向
dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

dydx4 = ((0, 1), (1, 0), (-1, 0), (0, -1))

# 8方向
dy = (0, 1, 1, 1, 0, -1, -1, -1)
dx = (1, 1, 0, -1, -1, -1, 0, 1)

dydx8 = ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1))


# 盤面からはみ出さないようにする
if ny < 0 or ny >= h or nx < 0 or nx >= w:
    continue


# 大きい値を採用する
ans = max(ans, tmp)


# 数字を一つずつ末尾に追加していく
# 元の数字に10をかけて実現
tmp = 10 * tmp + board[x][y]


# 幅優先探索
# https://atcoder.jp/contests/atc002/tasks/abc007_3

from collections import deque

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)


def grid_bfs(grid: list, sy: int, sx: int, INF: int = 1 << 60, wall: str = "#") -> list:
    h = len(grid)
    w = len(grid[0])

    q = deque()
    q.append((sy, sx))

    INF = 1 << 60  # 2**60

    dist = [[INF] * w for _ in range(h)]
    dist[sy][sx] = 0

    while len(q) > 0:
        # 次に探索する数字はキューからpopする
        y, x = q.popleft()

        # 最初の位置から四方の検索
        for di in range(4):
            ny = y + dy[di]
            nx = x + dx[di]

            # 盤面からはみ出さないようにする
            if ny < 0 or ny >= h or nx < 0 or nx >= w:
                continue
            if grid[ny][nx] == wall:
                continue
            if dist[ny][nx] != INF:
                continue

            dist[ny][nx] = dist[y][x] + 1
            q.append((ny, nx))

            # debug用
            for value in dist:
                print(*value)
            print("")

    return dist


def main():

    h, w = map(int, input().split())
    sy, sx = map(int, input().split())
    gy, gx = map(int, input().split())

    sy, sx = sy - 1, sx - 1
    gy, gx = gy - 1, gx - 1

    grid = [input() for _ in range(h)]

    dist = grid_bfs(grid, sy, sx)

    print(dist[gy][gx])


if __name__ == "__main__":
    main()

# ランレングス圧縮
from itertools import groupby


def rle(S: str) -> "List[tuple(str, int)]":
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, int(len(list(v)))))
    return res


# bit全探索

# 問題
# N個の硬貨があります、番号iの硬貨はA_i円です。
# 硬貨の選び方は2^N通りありますが、
# その中で合計価格がちょうどX円になる選び方は存在するでしょうか。

input_text = """
3 100
31 39 40 11 20 30
"""

def_input(input_text)

if __name__ == "__main__":
    # https://www.youtube.com/watch?v=mEdFo-IbRdo
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    # 2 ** n回分、回す
    # 1 << 5 == 2 ** 5
    for i in range(1 << n):
        # 硬貨を利用するかどうか、をuseに格納していく
        # 例えば、4個の硬貨(1, 10, 11, 100)が存在し、use=[False, True, True, False]の場合は
        # 10と11は利用する、という意味になる
        use = [False] * n

        for j in range(n):
            if i & (1 << j):
                use[j] = True

        # useを1次元配列→多次元配列にして、最初に作っておくのでもアリだけど、
        # この方法の方が巨大なuseを作らなくて済む

        # 例えばi=6, j=4とする
        # for j in range(n):のとき、(1 << j) → 1, 2, 4, 8となる

        # つまり、i(この場合は6=0110)に対し、
        # 1(0001), 2(0010), 4(0100)、8(1000)という、
        # 1が一つずつずれるマスクでスクリーニングを行っていく

        # 0110 6
        # 0001 1 → 0110と0001で共通する部分はないからFalse
        # 0010 2 → 0110と0010で共通する部分はあるためTrue
        # 0100 4 → 0110と0100で共通する部分はあるためTrue
        # 1000 8 → 0110と1000で共通する部分はないためFalse
        # それをuseに入れる

        total = 0
        for j in range(n):
            if use[j]:
                total += a[j]

        if total == x:
            print("Yes")
            exit()
    print("No")


# 動的計画法

# 問題
# https://atcoder.jp/contests/abc261/tasks/abc261_d

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

# グラフのデータの持ち方
if __name__ == "__main__":
    n, m = map(int, input().split())

    adj = [[False] * n for _ in range(n)]

    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u][v] = True
        adj[v][u] = True
