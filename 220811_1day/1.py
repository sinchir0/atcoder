from atcoder.atcoder_test import def_input, input

input_text = """
19 3 4
"""

def_input(input_text)

if __name__ == "__main__":
    N, A, B = map(int, input().split())

    gr_num = N // (A + B)
    rem = N % (A+B)

    if rem > A:
        print(gr_num * A + A)
    else:
        print(gr_num * A + rem)
