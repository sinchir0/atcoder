from atcoder.atcoder_test import def_input, input

input_text = """
7 8
2 2
4 5
########
#......#
#.######
#..#...#
#..##..#
##.....#
########
"""

def_input(input_text)

from collections import deque

if __name__ == "__main__":

    dy = (0, 1, 0, -1)
    dx = (1, 0, -1, 0)

    r, c = map(int, input().split())
    sy, sx = map(lambda x: int(x) - 1, input().split())
    gy, gx = map(lambda x: int(x) - 1, input().split())

    board_list = [list(input()) for _ in range(r)]

    d = deque()

    d.append((sy, sx))

    board_list[sy][sx] = 0

    while len(d) > 0:
        y, x = d.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if board_list[ny][nx] == ".":
                d.append((ny, nx))
                board_list[ny][nx] = board_list[y][x] + 1

    print(board_list[gy][gx])
