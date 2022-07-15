from atcoder.atcoder_test import def_input, input

# 問題
# N個の硬貨があります、番号iの硬貨はA_i円です。
# 硬貨の選び方は2^N通りありますが、
# その中で合計価格がちょうどX円になる選び方は存在するでしょうか。

input_text = """
3 100
31 39 40 11 20 30
"""

def_input(input_text)

if __name__ == "__main__":
    # https://www.youtube.com/watch?v=mEdFo-IbRdo
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    for i in range(1 << n):
        use = [False] * n

        for j in range(n):
            if i & (1 << j):
                use[j] = True

        # useを1次元配列→多次元配列にして、最初に作っておくのでもアリだけど、
        # この方法の方が巨大なuseを作らなくて済む

        # 例えばi=6, j=4とする
        # for j in range(n):のとき、(1 << j) → 1, 2, 4, 8となる

        # つまり、i(この場合は6=0110)に対し、
        # 1(0001), 2(0010), 4(0100)、8(1000)という、
        # 1が一つずつずれるマスクでスクリーニングを行っていく

        # 0110 6
        # 0001 1 → 0110と0001で共通する部分はないからFalse
        # 0010 2 → 0110と0010で共通する部分はあるためTrue
        # 0100 4 → 0110と0100で共通する部分はあるためTrue
        # 1000 8 → 0110と1000で共通する部分はないためFalse
        # それをuseに入れる

        total = 0
        for j in range(n):
            if use[j]:
                total += a[j]

        if total == x:
            print("Yes")
            exit()
    print("No")
