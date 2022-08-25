from atcoder.atcoder_test import def_input, input

input_text = """
10 7 100
"""

def_input(input_text)


def check(n: int, a: int, b: int, x: int) -> bool:
    price = a * n + b * len(str(n))

    return price <= x


if __name__ == "__main__":

    a, b, x = map(int, input().split())

    ok = 0
    ng = 10 ** 9 + 1

    while ng - ok > 1:
        mid = (ok + ng) // 2

        if check(mid, a, b, x):  # 整数midが買えるならば
            # okを厳しくしても問題ない
            ok = mid
        else:
            ng = mid

    print(ok)
