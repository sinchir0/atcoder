from atcoder.atcoder_test import def_input, input

input_text = """
100 10 100 180 1
"""

def_input(input_text)

if __name__ == "__main__":
    n, m, x, t, d = map(int, input().split())

    if x <= m <= n:
        print(t)
    else:
        print(t - d * (x - m))
