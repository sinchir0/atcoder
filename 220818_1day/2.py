from atcoder.atcoder_test import def_input, input

input_text = """
atcoderregularcontest
"""

def_input(input_text)

if __name__ == "__main__":
    S = list(input())

    set_S = set(S)

    for word in list("abcdefjhijklmnopqrstuvwxyz"):
        if word not in set_S:
            print(word)
            exit()
    print("None")
