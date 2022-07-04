from atcoder.atcoder_test import def_input, input

input_text = """
40
"""

def_input(input_text)

if __name__ == "__main__":
    x = int(input())
    h = 21 if x < 60 else 22
    m = x % 60
    print("{}:{:02}".format(h, m))
