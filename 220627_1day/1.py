# https://atcoder.jp/contests/abc139/submissions/32643095
from atcoder.atcoder_test import def_input, input

input_text = """
4 10
"""

def_input(input_text)


import math

if __name__ == "__main__":

    # 電源タップの口の数をAに 拡張したい口の数をBに代入
    A, B = map(int, input().split())

    # 必要な電源タップの最小値を切り上げで出力
    print(math.ceil((B - 1) / (A - 1)))
