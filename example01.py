""" The game -> Tic Tac Toe """


def output_tictactoe_3x3_console(list_of_cells: list):
    a_1, b_1, c_1, a_2, b_2, c_2, a_3, b_3, c_3 = list_of_cells
    print("{:-^7}".format("-"))
    print(f"|{a_1}|{b_1}|{c_1}|")
    print("{:-^7}".format("-"))
    print(f"|{a_2}|{b_2}|{c_2}|")
    print("{:-^7}".format("-"))
    print(f"|{a_3}|{b_3}|{c_3}|")
    print("{:-^7}".format("-"))


def determine_board_state(all_d):
    # --------------------
    a_1, b_1, c_1, a_2, b_2, c_2, a_3, b_3, c_3 = all_d
    if a_1 == a_2 == a_3 == "x" or b_1 == b_2 == b_3 == "x" or c_1 == c_2 == c_3 == "x":
        print("X wins")
    elif (
            a_1 == b_1 == c_1 == "x" or a_2 == b_2 == c_3 == "x" or a_3 == b_3 == c_3 == "x"
    ):
        print("X wins")
    elif a_1 == b_2 == c_3 == "x" or c_1 == b_2 == a_3 == "x":
        print("X wins")
    # ------------------
    elif (
            a_1 == a_2 == a_3 == "o" or b_1 == b_2 == b_3 == "o" or c_1 == c_2 == c_3 == "o"
    ):
        print('O wins"')
    elif (
            a_1 == b_1 == c_1 == "o" or a_2 == b_2 == c_3 == "o" or a_3 == b_3 == c_3 == "o"
    ):
        print('O wins"')
    elif a_1 == b_2 == c_3 == "o" or c_1 == b_2 == a_3 == "o":
        print('O wins"')
    # ------------------------
    elif " " not in all_d:
        print("Draw: Game board full")


def main(output_function):
    board = read_data()

    output_function(board)

    determine_board_state(board)


def read_data():
    try:
        with open("position.txt", "r") as fr:
            data = fr.read()
            d_list = []
            for i in data:
                if i == "\n":
                    continue
                i = i.replace(".", " ")
                d_list.append(i)
    except FileNotFoundError:
        print('File position.txt does not exist')
    return d_list


if __name__ == "__main__":
    main(output_function=output_tictactoe_3x3_console)
