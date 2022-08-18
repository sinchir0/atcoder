from atcoder.atcoder_test import def_input, input

input_text = """
catredo
"""

def_input(input_text)

if __name__ == "__main__":
    S = input()
    number_list = []
    x = {"a": 0, "t": 1, "c": 2, "o": 3, "d": 4, "e": 5, "r": 6}
    for w in S:
        number_list.append(x[w])

    cnt = 0

    for i in range(len(number_list)):
        for j in range(len(number_list) - i - 1):
            if number_list[j] > number_list[j + 1]:
                number_list[j], number_list[j + 1] = number_list[j + 1], number_list[j]
                cnt += 1
    print(cnt)
