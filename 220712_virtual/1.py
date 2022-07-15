from atcoder.atcoder_test import def_input, input

input_text = """
023456789
"""

def_input(input_text)

if __name__ == "__main__":
    s = set(list(input()))
    t = set([str(num) for num in range(10)])

    print((s ^ t).pop())
