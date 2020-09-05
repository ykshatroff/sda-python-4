""" The game -> Tic Tac Toe """


def pole(all_d):
    """ Fill the fields"""
    a_1, b_1, c_1, a_2, b_2, c_2, a_3, b_3, c_3 = all_d
    print("{:-^7}".format("-"))
    print(f"|{a_1}|{b_1}|{c_1}|")
    print("{:-^7}".format("-"))
    print(f"|{a_2}|{b_2}|{c_2}|")
    print("{:-^7}".format("-"))
    print(f"|{a_3}|{b_3}|{c_3}|")
    print("{:-^7}".format("-"))
    if a_1 == a_2 == a_3 == "x" or b_1 == b_2 == b_3 == "x" or c_1 == c_2 == c_3 == "x":
        print("X wins")
    elif (
            a_1 == b_1 == c_1 == "x" or a_2 == b_2 == c_3 == "x" or a_3 == b_3 == c_3 == "x"
    ):
        print("X wins")
    elif a_1 == b_2 == c_3 == "x" or c_1 == b_2 == a_3 == "x":
        print("X wins")
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
    elif " " not in all_d:
        print("Draw: Game board full")


if __name__ == "__main__":
    try:
        with open("position.txt", "r") as fr:
            data = fr.read()
            d_list = []
            for i in data:
                if i == "\n":
                    continue
                i = i.replace(".", " ")
                d_list.append(i)
        pole(d_list)
    except FileNotFoundError:
        print('File position.txt does not exist')
