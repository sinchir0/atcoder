from atcoder.atcoder_test import def_input, input

input_text = """
chokudai
"""

def_input(input_text)

import re

if __name__ == "__main__":
    w = input()
    ans = re.sub(r"a|i|u|e|o", "", w)

    print(ans)
