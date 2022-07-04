from atcoder.atcoder_test import def_input, input

input_text = """
4
2113
1314
7141
1519
"""

def_input(input_text)

if __name__ == "__main__":

    dy = (0, 1, 1, 1, 0, -1, -1, -1)
    dx = (1, 1, 0, -1, -1, -1, 0, 1)

    n = int(input())
    board = [list(map(lambda x: int(x), input())) for _ in range(n)]

    # 盤面の中での最大値を開始の値とする
    first_num = 0
    for i in range(n):
        for j in range(n):
            if first_num < board[i][j]:
                first_num = board[i][j]
                sy = i
                sx = j

    mx = 0
    for di in range(8):
        ny = sy + dy[di]
        nx = sx + dx[di]

        # トーラス型への対応
        ny = ny % n
        nx = nx % n

        if mx < board[ny][nx]:
            mx = board[ny][nx]
            ans_y = dy[di]
            ans_x = dx[di]

    ans_list = [first_num]
    ny = sy
    nx = sx

    for _ in range(n - 1):

        ny += ans_y
        nx += ans_x

        if ny > n - 1:
            ny = n - ny
        if nx > n - 1:
            nx = n - nx

        ans_list.append(board[ny][nx])

    ans_list = [str(value) for value in ans_list]

    print("".join(ans_list))
