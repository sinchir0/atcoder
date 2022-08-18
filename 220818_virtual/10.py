from atcoder.atcoder_test import def_input, input

input_text = """
3
1 0 0
"""

def_input(input_text)

if __name__ == "__main__":
    n = int(input())
    a = [0] + list(map(int, input().split()))

    res = [0] * (n+1)

    for i in range(n, 0, -1):
        sm = 0
        for j in range(i, n+1, i):
            sm += res[j]

        if sm%2 != a[i]:
            