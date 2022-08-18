from atcoder.atcoder_test import def_input, input

input_text = """
atcoderregularcontest
"""

def_input(input_text)

if __name__ == "__main__":
    S = list(input())

    exist = dict()
    for word in list("abcdefjhijklmnopqrstuvwxyz"):
        exist[word] = False

    for word in S:
        exist[word] = True

    for word, is_exist in exist.items():
        if is_exist == False:
            print(word)
            exit()
    print("None")
