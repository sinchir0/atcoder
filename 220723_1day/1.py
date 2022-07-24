from atcoder.atcoder_test import def_input, input

input_text = """
1
1
"""

def_input(input_text)

if __name__ == "__main__":
    n = int(input())
    a_list = list(map(int, input().split()))

    if n == 1:
        print(a_list[0])
        exit()

    a_list = sorted(a_list, reverse=True)

    alice_s = sum(a_list[::2])
    bob_s = sum(a_list[1::2])

    print(alice_s - bob_s)
