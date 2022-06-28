# input

# 数字一つ
a = int(input())

# 数字の列
a, b, c, d = map(int, input().split())

# 数字のlist
num_list = list(map(int, input().split()))

# 数字の配列のlist
num_arr_list = [list(map(int, input().split())) for _ in range(n)]

# 盤面のlist
board_list = [list(input()) for _ in range(r)]

# 1始まりを0始まりに変換
sy, sx = map(lambda x: int(x) - 1, input().split())


# 定数
ans = 1001001001  # ちょうど10桁と分かりやすく、32bitでもC言語だったらオーバーフローしない数字

# 切り上げ、切り捨て
N // W  # 切り捨て
-(-N // W)  # 切り上げ

# 方向の探索

# 4方向
dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

# 8方向
dy = (0, 1, 1, 1, 0, -1, -1, -1)
dx = (1, 1, 0, -1, -1, -1, 0, 1)

# 盤面からはみ出さないようにする
if ny < 0 or ny >= h or nx < 0 or nx >= w:
    continue


# 幅優先探索
# https://atcoder.jp/contests/atc002/tasks/abc007_3
from collections import deque

if __name__ == "__main__":

    dy = (0, 1, 0, -1)
    dx = (1, 0, -1, 0)

    h, w = map(int, input().split())
    sy, sx = map(lambda x: int(x) - 1, input().split())
    gy, gx = map(lambda x: int(x) - 1, input().split())

    board = [list(input()) for _ in range(h)]
    board[sy][sx] = 0

    d = deque()
    d.append((sy, sx))

    while len(d) > 0:
        # 次に探索する数字はキューからpopする
        y, x = d.popleft()

        # 最初の位置から四方の検索
        for di in range(4):
            ny = y + dy[di]
            nx = x + dx[di]

            if ny <= 0 or ny >= h or nx < 0 or nx >= w:
                continue

            # "."を発見したらキューにpushする
            if board[ny][nx] == ".":
                d.append((ny, nx))

                # boardの要素を現在の数字+1で置き換える
                board[ny][nx] = board[y][x] + 1

    print(board[gy][gx])
