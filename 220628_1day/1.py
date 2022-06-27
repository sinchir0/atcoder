from atcoder.atcoder_test import def_input, input

input_text = """
7
14 14 2 13 56 2 37
"""

def_input(input_text)

import math

if __name__ == "__main__":
    n = int(input())
    num_list = list(map(int, input().split()))

    mean_floor = math.floor(sum(num_list) / len(num_list))
    mean_ceil = math.ceil(sum(num_list) / len(num_list))

    hit_point_floor = sum([(num - mean_floor) ** 2 for num in num_list])
    hit_point_ceil = sum([(num - mean_ceil) ** 2 for num in num_list])

    print(min(hit_point_floor, hit_point_ceil))
