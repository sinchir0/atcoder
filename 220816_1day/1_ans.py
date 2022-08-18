from re import L

from atcoder.atcoder_test import def_input, input

input_text = """
31 -41 -59 26
"""

def_input(input_text)

if __name__ == "__main__":
    x1, y1, x2, y2 = map(int, input().split())
    dx = x2 - x1
    dy = y2 - y1

    x = x2
    y = y2

    ans = []
    for i in range(2):

        dx, dy = -dy, dx

        x = x + dx
        y = y + dy
        ans.append(x)
        ans.append(y)
    print(*ans)
