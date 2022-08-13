from atcoder.atcoder_test import def_input, input

input_text = """
1 2 3 3 5
"""

def_input(input_text)

from collections import Counter

if __name__ == "__main__":
    num = list(map(int, input().split()))
    c = Counter(num)
    cnt = list(c.values())
    if (cnt == [3, 2]) | (cnt == [2, 3]):
        print("Yes")
    else:
        print("No")
