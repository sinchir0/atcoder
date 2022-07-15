from atcoder.atcoder_test import def_input, input

input_text = """
459230781
"""

def_input(input_text)

if __name__ == "__main__":
    s = input()
    for i in range(10):
        if str(i) not in s:
            print(i)
