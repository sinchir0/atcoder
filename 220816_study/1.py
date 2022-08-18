from atcoder.atcoder_test import def_input, input

input_text = """
uncopyrightable
"""

def_input(input_text)

if __name__ == "__main__":
    S = input()
    s_l = len(S)
    set_s_l = len(set(list(S)))
    if s_l == set_s_l:
        print("yes")
    else:
        print("no")
