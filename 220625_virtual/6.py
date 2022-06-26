from atcoder.atcoder_test import def_input, input

input_text = """
1 1 7 2
"""

def_input(input_text)

if __name__ == "__main__":
    sx, sy, gx, gy = map(int, input().split())
    print((sy * gx + sx * gy) / (gy + sy))
