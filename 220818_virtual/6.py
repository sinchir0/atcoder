from atcoder.atcoder_test import def_input, input

input_text = """
123456789
"""

def_input(input_text)

if __name__ == "__main__":
    # N = list(input())
    # N = [int(val) for val in N]
    N = map(int, list(input()))
    if sum(N) % 9 == 0:
        print("Yes")
    else:
        print("No")
