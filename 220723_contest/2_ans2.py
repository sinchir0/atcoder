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
                if board[i][j] == "W" and board[j][i] == "L":
                    continue
                if board[i][j] == "L" and board[j][i] == "W":
                    continue
                if board[i][j] == "D" and board[j][i] == "D":
                    continue
                else:
                    print("incorrect")
                    exit()

    print("correct")
