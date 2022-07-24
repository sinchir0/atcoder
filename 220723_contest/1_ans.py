from atcoder.atcoder_test import def_input, input

input_text = """
0 3 1 2
"""

def_input(input_text)

if __name__ == "__main__":
    l1, r1, l2, r2 = map(int, input().split())
    print(max(0, min(r1, r2) - max(l1, l2)))
