from bisect import bisect_left, bisect_right


def lower_bound(a: list, key: int) -> int:
    n = len(a)

    ng = -1
    ok = n

    while ok - ng > 1:

        mid = (ok + ng) // 2

        if a[mid] >= key:
            ok = mid
        else:
            ng = mid
    return ok


def upper_bound(a: list, key: int) -> int:
    n = len(a)

    ng = -1
    ok = n

    while ok - ng > 1:

        mid = (ok + ng) // 2

        if a[mid] > key:
            ok = mid
        else:
            ng = mid
    return ok


def main():
    key = 5
    a = [0.2, 0.3, 4, 5.1, 9]

    print(lower_bound(a, key))  # 2
    print(bisect_left(a, key))
    print(upper_bound(a, key))  # 4
    print(bisect_right(a, key))


if __name__ == "__main__":
    main()
