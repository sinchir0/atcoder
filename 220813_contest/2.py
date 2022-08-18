from atcoder.atcoder_test import def_input, input

input_text = """
2 13
"""

def_input(input_text)

if __name__ == "__main__":
    maze = [
        ["###############"],
        ["#.............#"],
        ["#.###########.#"],
        ["#.#.........#.#"],
        ["#.#.#######.#.#"],
        ["#.#.#.....#.#.#"],
        ["#.#.#.###.#.#.#"],
        ["#.#.#.#.#.#.#.#"],
        ["#.#.#.###.#.#.#"],
        ["#.#.#.....#.#.#"],
        ["#.#.#######.#.#"],
        ["#.#.........#.#"],
        ["#.###########.#"],
        ["#.............#"],
        ["###############"],
    ]

    R, C = map(int, input().split())
    if maze[R - 1][0][C - 1] == "#":
        print("black")
    else:
        print("white")
