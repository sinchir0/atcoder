from atcoder.atcoder_test import def_input, input

input_text = """
8
8 2 7 3 4 5 6 1
"""

def_input(input_text)

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))

    idx_a = []
    for idx, val in enumerate(a):
        idx_a.append([idx + 1, val])

    idx_a = sorted(idx_a, key=lambda x: x[1])

    print(" ".join([str(val) for val, _ in idx_a]))
