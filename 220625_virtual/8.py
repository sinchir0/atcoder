from atcoder.atcoder_test import def_input, input

input_text = """
5 8
2 2
2 4
########
#.#....#
#.###..#
#......#
########
"""

def_input(input_text)

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
