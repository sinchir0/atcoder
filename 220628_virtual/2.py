from atcoder.atcoder_test import def_input, input

input_text = """
3 5
...#.
.#.#.
.#...
"""

def_input(input_text)

import copy
from collections import deque

if __name__ == "__main__":

    dy = (0, 1, 0, -1)
    dx = (1, 0, -1, 0)

    h, w = map(int, input().split())

    board_org = [list(input()) for _ in range(h)]

    d = deque()

    mx = 0

    for i in range(h):
        for j in range(w):

            board = copy.deepcopy(board_org)

            if board[i][j] != ".":
                continue

            # start地点を決める
            d.append((i, j))
            board[i][j] = 0

            while len(d) > 0:
                # 次に探索する数字はキューからpopする
                y, x = d.popleft()

                # 最初の位置から４方を探索
                for di in range(4):
                    ny = y + dy[di]
                    nx = x + dx[di]

                    if ny < 0 or ny >= h or nx < 0 or nx >= w:
                        continue

                    # "."を発見したらキューにpushする
                    if board[ny][nx] == ".":
                        d.append((ny, nx))

                        # boardの要素を現在の数字+1で置き換える
                        board[ny][nx] = board[y][x] + 1

                    if mx < (board[y][x]):
                        mx = board[y][x]

    print(mx)
