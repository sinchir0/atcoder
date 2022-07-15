from atcoder.atcoder_test import def_input, input

input_text = """
3000
"""

def_input(input_text)

if __name__ == "__main__":
    n = int(input())
    print(((n + 1000) // 1000) * 1000 - n)
