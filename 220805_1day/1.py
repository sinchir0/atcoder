from atcoder.atcoder_test import def_input, input

input_text = """
3 70
20 30 10
"""

def_input(input_text)

if __name__ == "__main__":
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    ans = 0

    for i in range(1 << n):
        use = [False] * n

        for j in range(n):
            if i & (1 << j):
                use[j] = True

        max_child = 0
        total = 0

        for j in range(n):
            if use[j]:
                total += a[j]
                max_child += 1

        if total == x:
            ans = max(ans, max_child)
        elif total <= x:
            ans = max(ans, max_child-1)

    print(ans)
