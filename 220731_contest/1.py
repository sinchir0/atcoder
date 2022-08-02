from atcoder.atcoder_test import def_input, input

input_text = """
2022
"""

def_input(input_text)

if __name__ == "__main__":
    y = int(input())

    a = y % 4

    if a == 0:
        print(y + 2)
    elif a == 1:
        print(y + 1)
    elif a == 2:
        print(y)
    elif a == 3:
        print(y + 3)