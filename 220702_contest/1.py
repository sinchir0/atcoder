from atcoder.atcoder_test import def_input, input

input_text = """
100
"""

def_input(input_text)

if __name__ == "__main__":
    k = int(input())

    h = k // 60
    if h >= 1:
        if k - 60 >= 10:
            print(f"{21+h}:{k-60}")
        else:
            print(f"{21+h}:0{k-60}")
    else:
        if k >= 10:
            print(f"21:{k}")
        else:
            print(f"21:0{k}")
