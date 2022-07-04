from atcoder.atcoder_test import def_input, input

input_text = """
3 3 0
100 -100 0
0 100 100
100 100 100
-100 100 100
"""

def_input(input_text)

if __name__ == "__main__":
    n, m, c = map(int, input().split())
    b = list(map(int, input().split()))
    a = [list(map(int, input().split())) for _ in range(n)]

    ans = 0
    for i in range(n):
        score = sum([b_i * a_i for b_i, a_i in zip(b, a[i])]) + c
        if score > 0:
            ans += 1

    print(ans)