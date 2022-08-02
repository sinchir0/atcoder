from atcoder.atcoder_test import def_input, input

input_text = """
4
1 3 2 4
"""

def_input(input_text)

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))

    for i in range(n):
        a[i] -= 1

    # 与えられた数列の中から, idxと値が一致する数を探す
    same = 0
    for (i, x) in enumerate(a):
        if i == x:
            same += 1

    # 一致する数から、順番を考慮し2個選ぶため、組み合わせの数はnP2 = n * (n-1) / 2
    ans = same * (same - 1) // 2

    # 配列aから、二つ目の条件を満たすものを探す
    for (i, j) in enumerate(a):
        # この中で、下記条件を満たすものが答え
        if i < j and a[j] == i:
            ans += 1

    print(ans)
