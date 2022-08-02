from atcoder.atcoder_test import def_input, input

input_text = """
4
1 3 2 4
"""

def_input(input_text)

if __name__ == "__main__":
    # 条件が成立するのは、下記の二つ
    # (1) a_i = i, a_j = j
    # (2) a_i = j, a_j = i

    # (1)の場合、一致する数の中から、順番を考慮して２つの組み合わせを選べば良いため、その数は(n * (n - 1)) / 2
    # (2)の場合、i < jの条件下で、a_j = iとなれば良い

    n = int(input())
    a = list(map(lambda x: int(x) - 1, input().split()))

    # (1)
    cnt = 0
    for i, j in enumerate(a):
        if i == j:
            cnt += 1

    ans = cnt * (cnt - 1) // 2

    # (2)
    for i, j in enumerate(a):
        # if i < j and a[j] == i:
        if a[a[i]] == i:
            ans += 1

    print(ans)
