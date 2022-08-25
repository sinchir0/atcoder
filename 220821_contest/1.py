from atcoder.atcoder_test import def_input, input

input_text = """
10 3 2
"""

def_input(input_text)

if __name__ == "__main__":
    X, Y, N = map(int, input().split())
    if X * 3 <= Y:
        print(X * N)
    else:
        div, remain = N // 3, N % 3
        print(div * Y + remain * X)
