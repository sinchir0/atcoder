from atcoder.atcoder_test import def_input, input

input_text = """
2 1 6
"""

def_input(input_text)

if __name__ == "__main__":
    A, B, C = map(int, input().split())
    tmp = min(A, B)
    print(C // tmp)
