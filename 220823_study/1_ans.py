from atcoder.atcoder_test import def_input, input

input_text = """
7
218 786 704 233 645 728 389
"""

def_input(input_text)

# https://blog.hamayanhamayan.com/entry/2019/10/19/224640_2
if __name__ == "__main__":
    N = int(input())
    L = list(map(int, input().split()))

    cnt = [0] * (2 * 10 ** 3 + 1)
    for i in range(N):
        cnt[L[i]] += 1

    # cntを累積和に変換、cnt[i]は、iの長さまでの棒が合計何本あるか、を意味する
    for i in range(1, len(cnt)):
        cnt[i] += cnt[i - 1]

    ans = 0
    for a in range(N):
        for b in range(N):
            if a != b:
                mi = max(L[a] - L[b], L[b] - L[a])
                ma = L[a] + L[b]

                # cnはmax(a-b, b-a) < c < a+bを満たすcの数
                cn = 0
                # まず、c < a+bを満たすcの数をcnに入れる
                # ma = a+b
                # ma - 1 は、c < a + bが何個あるかを調べるため、-1を行なっている
                # 仮にcnt[ma]だと、c <= a + bの数を計算してしまう
                if 0 <= ma - 1:
                    cn = cnt[ma - 1]
                # max(a-b, b-a) < cを満たす数を引く
                cn -= cnt[mi]

                # aで選択した棒が、cの候補に入る場合は-1する
                if (mi < L[a]) and (L[a] < ma):
                    cn -= 1
                # bで選択した棒が、cの候補に入る場合は-1する
                if (mi < L[b]) and (L[b] < ma):
                    cn -= 1

                ans += cn

    ans = ans // 6
    print(ans)
