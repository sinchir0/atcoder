from atcoder.atcoder_test import def_input, input

input_text = """
5
8 9 18 90 72

"""

def_input(input_text)

from collections import defaultdict

if __name__ == "__main__":
    n = int(input())
    a_list = list(map(int, input().split()))
    a_list = sorted(a_list)

    if len(set(a_list)) == 1:
        print(a_list[0])
        exit()

    half_num = a_list[len(a_list) // 2]

    val_cnt = defaultdict(int)

    for i in range(2, half_num + 1):
        for a_num in a_list:
            if a_num % i == 0:
                val_cnt[i] += 1
    print(max(val_cnt, key=val_cnt.get))
