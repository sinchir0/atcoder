from atcoder.atcoder_test import def_input, input

input_text = """
10 7 5
1 2 3 4 6 8 9
"""

def_input(input_text)

if __name__ == "__main__":
    n, m, x = map(int, input().split())
    a = list(map(int, input().split()))

    load = [0] * (n + 1)
    for idx in a:
        load[idx] = 1

    print(min(sum(load[:x]), sum(load[x:])))
