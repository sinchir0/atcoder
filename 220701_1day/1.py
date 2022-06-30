from atcoder.atcoder_test import def_input, input

input_text = """
1001
"""

def_input(input_text)

if __name__ == "__main__":
    n = int(input())

    for ans in range(1, n + 1):
        val = ans * 108 // 100
        if val == n:
            print(ans)
            exit()
    print(":(")
