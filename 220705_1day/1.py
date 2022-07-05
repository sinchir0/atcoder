from atcoder.atcoder_test import def_input, input

input_text = """
4 5
"""

def_input(input_text)

if __name__ == "__main__":
    h, w = map(int, input().split())

    if (h == 1) | (w == 1):
        print(1)
        exit()

    all = h * w
    print((all + 2 - 1) // 2)