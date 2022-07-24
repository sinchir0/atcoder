from atcoder.atcoder_test import def_input, input

input_text = """
3 2
1000000000 1000000000 1000000000
1 1000000000
3 1000000000
"""

def_input(input_text)

from collections import defaultdict, deque

if __name__ == "__main__":

    n, m = map(int, input().split())
    x_arr = list(map(int, input().split()))

    x_dict = defaultdict(int)
    for idx, val in enumerate(x_arr):
        x_dict[idx] = val

    bonus = defaultdict(int)
    for _ in range(m):
        c, y = map(int, input().split())
        bonus[c] = y

    q = deque()
    # num, cnt, idx
    q.append((0, 0, 0))

    ans = 0

    while len(q) > 0:
        # 次に探索する数字はキューからpopする
        num, cnt, idx = q.popleft()

        if idx >= n:
            continue

        # 表か裏か
        for coin in (1, 0):
            # 表の場合
            if coin == 1:
                next_num = x_dict[idx] + num
                next_cnt = cnt + 1

                # ボーナスの考慮
                if next_cnt != 0:
                    next_num += bonus[next_cnt]

            # 裏の場合
            elif coin == 0:
                cnt = 0

                next_num = num
                next_cnt = cnt

            q.append((next_num, next_cnt, idx + 1))

            ans = max(next_num, ans)

    print(ans)
