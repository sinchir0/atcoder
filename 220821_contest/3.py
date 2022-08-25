from atcoder.atcoder_test import def_input, input

input_text = """
2 3
RRD
ULL
"""

def_input(input_text)

if __name__ == "__main__":
    H, W = map(int, input().split())
    board = [list(input()) for _ in range(H)]

    idx = (1, 1)

    cnt = 0
    # while cnt < 10 ** 8:
    while cnt < 10 ** 6:
        cnt += 1
        word = board[idx[0] - 1][idx[1] - 1]

        if word == "U" and idx[0] != 1:
            idx = idx[0] - 1, idx[1]
        elif word == "D" and idx[0] != H:
            idx = idx[0] + 1, idx[1]
        elif word == "L" and idx[1] != 1:
            idx = idx[0], idx[1] - 1
        elif word == "R" and idx[1] != W:
            idx = idx[0], idx[1] + 1
        else:
            print(*idx)
            exit()

    print(-1)
