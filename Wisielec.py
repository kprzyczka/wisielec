#python_lst236.pyt

import random

def hangman(word):
    wrong = 0
    stages = ["",
            "______   ",
            "|    |   ",
            "|    |   ",
            "|    0   ",
            "|   /|\  ",
            "|   / \  "
            ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("gra w wisielca")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "Odgadnij literę: "
        char = input(msg).lower()
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "_" not in board:
            print("Wygrałeś!")
            print("słowo to"," ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("Przegrałeś! Miałeś odgadnąć słowo: {}.".format(word))

lista_slow= ["duppa","pupa","test", "best"]
hangman(random.choice(lista_slow))
