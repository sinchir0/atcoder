from atcoder.atcoder_test import def_input, input

input_text = """
10
"""

def_input(input_text)

if __name__ == "__main__":
    N = int(input())
    print(((1 + N)*10 // 2) * 1000)
