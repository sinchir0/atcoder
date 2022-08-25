from atcoder.atcoder_test import def_input, input

input_text = """
6
1
4
3
7
4
2
"""

def_input(input_text)

if __name__ == "__main__":

    N = int(input())
    A = []
    for _ in range(N):
        A.append(int(input()))

    lft = A.copy()
    for i in range(1, N):
        lft[i] = max(lft[i], lft[i - 1])

    rht = A.copy()
    for i in range(N - 2, 0, -1):
        rht[i] = max(rht[i], rht[i + 1])

    for i in range(N):
        ans = -1
        # iが左端のとき以外
        if i != 0:
            # 答えに、一旦i-1までの最大値を入れる
            ans = max(ans, lft[i - 1])
        # iが右端のとき以外
        if i + 1 != N:
            # 上のifで出したi-1までの最大値と、i+1より大きい部分の最大値のうち、大きい方を答えにする
            ans = max(ans, rht[i + 1])
        print(ans)
