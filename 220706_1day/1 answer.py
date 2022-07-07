from re import L

from atcoder.atcoder_test import def_input, input

input_text = """
41 7 46
26 89 2
78 92 8
5
6
45
16
57
17
"""

def_input(input_text)

if __name__ == "__main__":
    bingo = [list(map(int, input().split())) for _ in range(3)]
    n = int(input())

    for _ in range(n):
        b = int(input())
        for i in range(3):
            for j in range(3):
                if bingo[i][j] == b:
                    bingo[i][j] = True

    # 横の判定
    for i in range(3):
        if bingo[i][0] == bingo[i][1] == bingo[i][2]:
            print("Yes")
            exit()

    # 縦の判定
    for j in range(3):
        if bingo[0][j] == bingo[1][j] == bingo[2][j]:
            print("Yes")
            exit()

    # 斜めの判定
    if (bingo[0][0] == bingo[1][1] == bingo[2][2]) or (
        bingo[0][2] == bingo[1][1] == bingo[2][0]
    ):
        print("Yes")
        exit()

    print("No")
