from atcoder.atcoder_test import def_input, input

input_text = """
3 3 10
60 2 2 4
70 8 7 9
50 2 3 9
"""

def_input(input_text)

from collections import deque

if __name__ == "__main__":
    n, m, x = map(int, input().split())
    num_arr_list = [list(map(int, input().split())) for _ in range(n)]

    d = deque()

    ans_list = ["nan"] * n

    for i in range(n):
        # start地点を決める
        d.append(num_arr_list[i])
        ans_list[i] = num_arr_list[0][0]

        while len(d) > 0:
            # 次に探索する数字はキューからpopする
            value = d.popleft()
            breakpoint()

            # 最初の位置から４方を探索
            for di in range(i):
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
