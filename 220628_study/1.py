from atcoder.atcoder_test import def_input, input

input_text = """
0 0 0
"""

def_input(input_text)

from collections import Counter

if __name__ == "__main__":
    num_list = list(map(int, input().split()))

    num_cnt = Counter(num_list)

    if len(num_cnt) == 1:
        print(num_list[0])
    elif sum(num_list) <= 1:
        print(-1)
    elif len(num_cnt) == 2:
        A = num_cnt.most_common()[0][0]
        B = num_cnt.most_common()[1][0]

        if B - A == 1:
            print(B)
        elif B < A:
            print(A)
    else:
        print(-1)
