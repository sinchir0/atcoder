from atcoder.atcoder_test import def_input, input

input_text = """
3 3
1 1 1
1 1 1
1 1 1
1 1
2
"""

def_input(input_text)

if __name__ == "__main__":
    H1, W1 = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H1)]
    H2, W2 = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(H2)]

    N = H1 + W1

    for i in range(1 << N):
        tmp = []
        use = [False] * N

        for j in range(N):
            if i & (1 << j):
                use[j] = True

        # 行の選択
        for r in range(H1):
            if use[r]:
                tmp.append(A[r])

        # 列の選択
        ans = []
        if tmp:
            for row in tmp:
                tmp = [val for idx, val in enumerate(row) if use[H1:][idx]]
                ans.append(tmp)

        if ans == B:
            print("Yes")
            exit()
    print("No")
