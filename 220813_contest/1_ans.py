from atcoder.atcoder_test import def_input, input

input_text = """
1 2
"""

def_input(input_text)

if __name__ == "__main__":
    L, R = map(int, input().split())

    print("".join(["atcoder"[i] for i in range(L - 1, R)]))
