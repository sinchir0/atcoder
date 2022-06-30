# https://atcoder.jp/contests/abc161/submissions/32816612

from atcoder.atcoder_test import def_input, input

input_text = """
"""

def_input(input_text)

from collections import deque


def main():
    k = int(input())

    cnt = 9

    if k <= cnt:
        print(k)
        exit()

    q = deque(list(range(1, 10)))
    while len(q) > 0:
        # queueの一番左の値を出力
        v = q.popleft()

        for diff in (-1, 0, 1):
            # vから下一桁を取得するために%10を行う
            nv = v % 10 + diff

            # nvの値が0より小さい、もしくは10以上の場合は計算しない
            if nv < 0 or nv >= 10:
                continue

            # 例えば、1に2を繋げた12を出力したい場合、1(ここではv)に対し10をかける必要がある
            next_num = v * 10 + nv
            # queueの一番右の値を入力
            q.append(next_num)
            cnt += 1

            # 問題文で指定されたk回の数字を出力
            if cnt == k:
                print(next_num)
                exit()


if __name__ == "__main__":
    main()
