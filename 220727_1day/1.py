from atcoder.atcoder_test import def_input, input

input_text = """
7 4
"""

def_input(input_text)

if __name__ == "__main__":
    n, k = map(int, input().split())

    t = n % k
    print(min(t, k - t))
