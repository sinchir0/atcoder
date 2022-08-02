from atcoder.atcoder_test import def_input, input

input_text = """
5
1 4 6 7 9
"""

def_input(input_text)

if __name__ == "__main__":
    n = int(input())
    d = list(map(int, input().split()))

    d = sorted(d)

    half_n = n // 2
    print(d[half_n] - d[half_n - 1])
