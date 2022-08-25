# https://atcoder.jp/contests/abc265/submissions/34249912
# これを見ながら解く

from atcoder.atcoder_test import def_input, input

input_text = """
9 44
RRDDDDRRRDDDRRRRRRDDDRDDDDRDDRDDDDDDRRDRRRRR
RRRDLRDRDLLLLRDRRLLLDDRDLLLRDDDLLLDRRLLLLLDD
DRDLRLDRDLRDRLDRLRDDLDDLRDRLDRLDDRLRRLRRRDRR
DDLRRDLDDLDDRLDDLDRDDRDDDDRLRRLRDDRRRLDRDRDD
RDLRRDLRDLLLLRRDLRDRRDRRRDLRDDLLLLDDDLLLLRDR
RDLLLLLRDLRDRLDDLDDRDRRDRLDRRRLDDDLDDDRDDLDR
RDLRRDLDDLRDRLRDLDDDLDDRLDRDRDLDRDLDDLRRDLRR
RDLDRRLDRLLLLDRDRLLLRDDLLLLLRDRLLLRRRRLLLDDR
RRRRDRDDRRRDDRDDDRRRDRDRDRDRRRRRRDDDRDDDDRRR
"""

def_input(input_text)

if __name__ == "__main__":
    H, W = map(int, input().split())

    visit = [[False] * W for _ in range(H)]

    board = [list(input()) for _ in range(H)]

    idx = (0, 0)

    while True:
        i = idx[0]
        j = idx[1]
        if visit[i][j] == True:
            print(-1)
            exit()

        visit[i][j] = True

        word = board[i][j]
        if word == "U" and i != 0:
            idx = (i - 1, j)
        elif word == "D" and i != H - 1:
            idx = (i + 1, j)
        elif word == "L" and j != 0:
            idx = (i, j - 1)
        elif word == "R" and j != W - 1:
            idx = (i, j + 1)
        else:
            print(i + 1, j + 1)
            exit()
