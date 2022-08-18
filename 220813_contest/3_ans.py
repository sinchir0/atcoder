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

    for i in range(1 << H1):
        # 行の選択
        use_row = []
        for j in range(H1):
            if i & (1 << j):
                use_row.append(j)

        for k in range(1 << W1):
            # 列の選択
            use_col = []
            for r in range(W1):
                if k & (1 << r):
                    use_col.append(r)

            if (len(use_row) != H2) | (len(use_col) != W2):
                continue

            flg = True
            for row in range(H2):
                for col in range(W2):
                    if B[row][col] != A[use_row[row]][use_col[col]]:
                        flg = False
            if flg:
                print("Yes")
                exit()
    print("No")
