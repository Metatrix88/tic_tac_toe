import os
the_board = [i for i in range(1, 10)]
menu_answers = {"1": "statistic", "2": "playgame"}

def get_answer():
    answer = input("Your choise: ")
    return menu_answers.get(answer)

def show_menu():
    os.system("cls")
    print("___MENU___")
    print("1. Show statistic")
    print("2. Play the game\n")

    answer = get_answer()
    while not answer:
        print("Pls pick the right option")
        answer = get_answer()
    return answer

def show_the_board():
    print("-" * 13)
    for i in range(3):
        print("|", the_board[0+i*3], "|", the_board[1+i*3], "|", the_board[2+i*3], "|")
        print("-" * 13)


def show_statistic():
    player_x = "X"
    player_y = "O"
    Draw = "Draw"
    if  check_win() == 'X':
        player_x = int(player_x + 1)
        print(f"Player_x win {player_x}")
    elif check_win() == 'O':
        player_y = int(player_y + 1)
        print(f"Player_y win {player_y}")
    elif check_win() == 'draw':
        Draw = Draw + 1
    return player_x, player_y, Draw

def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input("Please choose the cell: " + player_token + "?")
        try:
            player_answer = int(player_answer)
        except:
            print("Incorrect date. Please enter numbers, please enter numbers from 1 to 9.")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if(str(the_board[player_answer-1]) not in "XO"):
                the_board[player_answer-1] = player_token
                valid = True
            else:
                print("This cell has been already booked")
        else:
            print("Please enter numbers from 1 to 9.")

def check_win():
    win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,6,4))
    for each in win_coord:
        if the_board[each[0]] == the_board[each[1]] == the_board[each[2]]:
            return the_board[each[0]]
    return False

def play_the_game():
    counter = 0
    win = False
    while not win:
        show_the_board()
        if counter % 2 == 0:
            print("Player 1: Please choose empty cell: ")
            take_input("X")
        else:
            print("Player 2: Please choose empty cell: ")
            take_input("O")
        counter += 1

        if counter > 4:
            tmp = check_win()
            if tmp:
                print(tmp, "You win!")
                win = True
                break
        if counter == 9:
            print("Draw")
            break
    show_the_board()

def main():
    answer = show_menu()
    if answer == "statistic":
        show_statistic()
    else:
        play_the_game()

if __name__ == '__main__':
    main()
