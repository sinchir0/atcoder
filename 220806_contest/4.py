from atcoder.atcoder_test import def_input, input

input_text = """
5 4 3
5 5 0 6 3
"""

def_input(input_text)

if __name__ == "__main__":
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))

    fin_ans = 10 ** 10
    for j in range(n):
        for i in range(0, n - j):
            ans = 0
            ans += l * i

            ans += r * j

            ans += sum(a[i : n - j])
            fin_ans = min(ans, fin_ans)

    print(fin_ans)
