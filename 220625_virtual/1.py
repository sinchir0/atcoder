from atcoder.atcoder_test import def_input, input

input_text = """
200 300
"""

def_input(input_text)

if __name__ == "__main__":
    a, b = map(int, input().split())
    print((2 * a + 100) - b)
