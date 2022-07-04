from atcoder.atcoder_test import def_input, input

input_text = """
10 8
dsuccxulnl
2 4
2 7
1 2
2 7
1 1
1 2
1 3
2 5
"""

def_input(input_text)

# 普通に解くと、O(N * Q)になり、2≤N≤5×10^5, 1≤Q≤5×10^5のため、TLE
# NもQも大きいため、クエリ自体は必ず処理すると考え、O(Q)を目標とする

if __name__ == "__main__":
    n, q = map(int, input().split())
    s = input()

    start = 0

    for _ in range(q):
        t, x = map(int, input().split())
        if t == 1:
            # rotateしていると考え、abc → cabになるため、startの位置がc始まりになるようにする
            start -= x
            start %= n
        elif t == 2:
            # startの位置を基準に、どの位置の文字を出すかを決める
            output_idx = start + x - 1

            # ただし、nよりも大きくなった場合は循環させる
            output_idx %= n

            print(s[output_idx])
