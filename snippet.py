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
n // w  # 切り捨て
(n + w - 1) // w  # 切り上げ

# 小数点以下の計算をしないために
# もし100 * 1.08をしたい場合は
100 * 108 // 100

# >>> 100 * 108 // 100
# 108

# >>> 100 * 1.08
# 108.0

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
