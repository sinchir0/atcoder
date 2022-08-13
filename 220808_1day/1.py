from atcoder.atcoder_test import def_input, input

input_text = """
5
30 44
26
18
81
18
6
"""

def_input(input_text)

if __name__ == "__main__":
    N = int(input())
    D, X = map(int, input().split())
    use_cho = 0
    for _ in range(N):
        use_cho += 1 + (D - 1) // int(input())
    print(use_cho + X)
