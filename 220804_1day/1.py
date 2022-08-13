from atcoder.atcoder_test import def_input, input

input_text = """
99992
"""

def_input(input_text)

if __name__ == "__main__":
    x = int(input())

    for n in range(x, 10 ** 6):
        flag = True
        for i in range(2, n):
            if n % i == 0:
                flag = False
                break
        if flag:
            print(n)
            exit()
