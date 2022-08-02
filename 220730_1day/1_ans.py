from atcoder.atcoder_test import def_input, input

input_text = """
8
8 2 7 3 4 5 6 1
"""

def_input(input_text)

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))

    ans = [0] * n
    for i in range(n):
        ans[a[i] - 1] = i + 1

    print(*ans)
