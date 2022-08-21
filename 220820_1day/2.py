from atcoder.atcoder_test import def_input, input

input_text = """
10
10
10
10
10
"""

def_input(input_text)


def round_up(num: int) -> int:
    return ((num + 10 - 1) // 10) * 10


if __name__ == "__main__":
    num = [int(input()) for _ in range(5)]

    remain = 0
    max_idx = 0
    for idx, val in enumerate(num):
        tmp = round_up(val) - val
        if tmp > remain:
            max_idx = idx
            remain = tmp

    ans = [round_up(val) if idx != max_idx else val for idx, val in enumerate(num)]
    print(sum(ans))