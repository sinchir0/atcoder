from atcoder.atcoder_test import def_input, input

input_text = """
3 5
"""

def_input(input_text)

if __name__ == "__main__":
    # bit全探索
    N, M = map(int, input().split())

    ans = []

    for use in range(1 << M):
        # useはbit
        tmp = []
        # j桁目に1があるかどうかを確認
        for j in range(M):
            if (use >> j) % 2 == 1:
                tmp.append(j)

        if len(tmp) == N:
            ans.append(tmp)

    ans = sorted(ans)

    for nums in ans:
        for i in range(N):
            nums[i] += 1
        print(*nums)
