from atcoder.atcoder_test import def_input, input

input_text = """
31 -41 -59 26
"""

def_input(input_text)

if __name__ == "__main__":
    x1, y1, x2, y2 = map(int, input().split())
    x3 = x2 - (y2 - y1)
    y3 = y2 + (x2 - x1)

    x4 = x3 - (x2 - x1)
    y4 = y3 - (y2 - y1)
    print(x3, y3, x4, y4)