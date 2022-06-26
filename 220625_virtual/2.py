from atcoder.atcoder_test import def_input, input

input_text = """
10000 1 1
"""

def_input(input_text)

if __name__ == "__main__":
    d, t, s = map(int, input().split())
    if d / s <= t:
        print("Yes")
    else:
        print("No")
