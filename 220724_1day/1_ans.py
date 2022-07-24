from atcoder.atcoder_test import def_input, input

input_text = """
3
"""

def_input(input_text)

if __name__ == "__main__":
    n = int(input())

    c = 2

    if n == 1:
        print(1)
        exit()
        
    while True:
        c = c * 2
        if n < c * 2:
            print(c)
            exit()
