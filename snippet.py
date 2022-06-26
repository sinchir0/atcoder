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
