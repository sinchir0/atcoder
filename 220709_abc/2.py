from atcoder.atcoder_test import def_input, input

input_text = """
2 2 180
"""

def_input(input_text)

import math

if __name__ == "__main__":
    a, b, d = map(int, input().split())

    radian_d = math.radians(d)

    x = math.cos(radian_d) * a - math.sin(radian_d) * b
    y = math.sin(radian_d) * a + math.cos(radian_d) * b

    print(x, y)
