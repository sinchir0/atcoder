# https://www.youtube.com/watch?v=Hs4XsziFpPo
# aの中にkeyが存在する位置を返す
def binary_search(a: list, key: int) -> int:
    n = len(a)

    l = -1  # 左手、元のaから一個左にはみ出す
    r = n  # 右手、aの最後のindex+1

    # 右手と左手の範囲を少しずつ狭めていき、同じ値になったら終了
    while r - l > 1:
        m = (l + r) // 2

        if a[m] == key:
            return m

        if a[m] > key:
            r = m
        else:
            l = m

    return -1


if __name__ == "__main__":
    a = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    a = sorted(a)

    key = 1
    print(binary_search(a, key))

    import numpy as np
