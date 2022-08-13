from atcoder.atcoder_test import def_input, input

input_text = """
2 10
"""

def_input(input_text)


def dfs(A):
    if len(A) == N:
        print(*A)
        return
    if len(A) == 0:
        start = 1
    else:
        start = A[-1] + 1
    for i in range(start, M + 1):
        dfs(A + [i])


if __name__ == "__main__":
    N, M = map(int, input().split())
    dfs([])
