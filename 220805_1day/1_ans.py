from atcoder.atcoder_test import def_input, input

input_text = """
3 10
20 30 10
"""

def_input(input_text)

if __name__ == "__main__":
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    if x == sum(a):
        print(n)
    elif x > sum(a):
        print(n - 1)
    else:
        sum_val = 0
        ans = 0
        for val in sorted(a):
            sum_val += val
            ans += 1
            if sum_val > x:
                print(ans - 1)
                exit()
