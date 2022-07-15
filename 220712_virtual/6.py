from atcoder.atcoder_test import def_input, input

input_text = """
100000
"""

def_input(input_text)

import math

if __name__ == "__main__":
    n = int(input())
    ans = math.factorial(n)
    print(ans % (10**9 + 7))
