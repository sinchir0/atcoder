from atcoder.atcoder_test import def_input, input

input_text = """
2 13
"""

def_input(input_text)

if __name__ == "__main__":
    R, C = map(int, input().split())

    if max(abs(R - 8), abs(C - 8)) % 2 == 1:
        print("black")
    else:
        print("white")
