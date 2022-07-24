from atcoder.atcoder_test import def_input, input

input_text = """
4
-WWW
L-DW
LD-L
LDW-
"""

def_input(input_text)

if __name__ == "__main__":
    n = int(input())

    board = [list(input()) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i > j:
                if board[i][j] == "W":
                    if board[j][i] = "L":
                        print("incorrect")
                        exit()
                if board[i][j] == "L":
                    if board[j][i] != "W":
                        print("incorrect")
                        exit()
                if board[i][j] == "D":
                    if board[j][i] != "D":
                        print("incorrect")
                        exit()

    print("correct")
