from atcoder.atcoder_test import def_input, input

input_text = """
2 2 1
3 5
3 5
2 2 2
"""

def_input(input_text)

if __name__ == "__main__":
    A, B, M = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    x = [list(map(int, input().split())) for _ in range(M)]

    # a, bから最小値の組み合わせを見つける
    min_num = min(a) + min(b)

    ans = min_num
    # 割引券を適用した場合の値と比較し、min_numよりも小さい値があれば更新
    for val in x:
        cand = a[val[0] - 1] + b[val[1] - 1] - val[2]
        ans = min(ans, cand)
    print(ans)
