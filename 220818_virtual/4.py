from atcoder.atcoder_test import def_input, input

input_text = """
3
4
"""

def_input(input_text)

if __name__ == "__main__":
    N = int(input())
    A = int(input())

    print(N * N - A)
