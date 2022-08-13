from atcoder.atcoder_test import def_input, input

input_text = """
1
"""

def_input(input_text)


def even(n: int):
    return n // 2


def odd(n: int):
    return 3 * n + 1


if __name__ == "__main__":
    s = int(input())

    a = set()
    a.add(s)

    cnt = 1
    while True:
        cnt += 1
        if s % 2 == 0:
            s = even(s)
        else:
            s = odd(s)

        past_len = len(a)
        a.add(s)

        if len(a) == past_len:
            print(cnt)
            exit()